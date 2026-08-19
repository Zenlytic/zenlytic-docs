#!/usr/bin/env python3
"""Post-process an exported OpenAPI spec with GitBook rendering niceties.

Reads the OpenAPI document produced by the backend's export script, merges in
hand-authored narrative content from ./content, synthesizes per-operation
x-codeSamples and a servers {% tabs %} block, and writes the enriched result
to a separate output path. Modeled on GitBook's reference spec:
https://gitbookio.github.io/onboarding-template-images/gitbook-petstore.yaml

Usage:
    python3 enrich.py --input developers/openapi.yaml --output developers/openapi.gitbook.yaml
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
SERVERS_TABS_TOKEN = "{{SERVERS_TABS}}"
PLACEHOLDER_TOKEN = "YOUR_TOKEN"


class _BlockLiteralDumper(yaml.SafeDumper):
    pass


def _str_presenter(dumper, data):
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_BlockLiteralDumper.add_representer(str, _str_presenter)


def load_doc(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def dump_doc(doc, path):
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(
            doc,
            f,
            Dumper=_BlockLiteralDumper,
            sort_keys=False,
            allow_unicode=True,
            width=100,
        )


def load_yaml_content(path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_text_content(path):
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def resolve_ref(node, doc):
    if isinstance(node, dict) and "$ref" in node:
        ref = node["$ref"]
        if not ref.startswith("#/"):
            return node
        target = doc
        for part in ref[2:].split("/"):
            target = target[part]
        return target
    return node


def example_from_schema(schema, doc):
    schema = resolve_ref(schema, doc) if schema else None
    if not schema:
        return None, False
    if "example" in schema:
        return schema["example"], True
    examples = schema.get("examples")
    if isinstance(examples, list) and examples:
        return examples[0], True
    if isinstance(examples, dict) and examples:
        first = next(iter(examples.values()))
        return first, True
    return None, False


def build_servers_tabs(servers):
    if len(servers) < 2:
        return None
    lines = ["{% tabs %}"]
    for i, server in enumerate(servers):
        title = server.get("description") or server["url"]
        lines.append(f'{{% tab title="{title}" %}}')
        lines.append("**Base URL**")
        lines.append(f'`{server["url"]}`')
        lines.append("{% endtab %}")
        if i != len(servers) - 1:
            lines.append("")
    lines.append("{% endtabs %}")
    return "\n".join(lines)


def apply_intro(doc, content_dir):
    intro_path = content_dir / "intro.md"
    intro = load_text_content(intro_path)
    if intro is None:
        return
    tabs_block = build_servers_tabs(doc.get("servers", []))
    intro = intro.replace(SERVERS_TABS_TOKEN, tabs_block if tabs_block else "")
    doc.setdefault("info", {})["description"] = intro


def apply_operation_notes(doc, content_dir):
    notes = load_yaml_content(content_dir / "operation-notes.yaml")
    if not notes:
        return
    for path_item in doc.get("paths", {}).values():
        for method, operation in path_item.items():
            if method not in HTTP_METHODS:
                continue
            op_id = operation.get("operationId")
            note = notes.get(op_id)
            if not note:
                continue
            note = note.rstrip("\n")
            existing = operation.get("description", "")
            if note in existing:
                continue  # already appended - keep this idempotent
            operation["description"] = f"{existing.rstrip()}\n\n{note}" if existing else note


def path_params_for_operation(path_item, operation):
    params = list(path_item.get("parameters", [])) + list(operation.get("parameters", []))
    return [p for p in params if p.get("in") == "path"]


def param_example_value(param, doc):
    schema = param.get("schema")
    if schema:
        value, found = example_from_schema(schema, doc)
        if found:
            return value
    if "example" in param:
        return param["example"]
    examples = param.get("examples")
    if isinstance(examples, dict) and examples:
        first = next(iter(examples.values()))
        if isinstance(first, dict) and "value" in first:
            return first["value"]
    return f"<{param['name']}>"


def build_url(base_url, path, path_item, operation, doc):
    for param in path_params_for_operation(path_item, operation):
        value = param_example_value(param, doc)
        path = path.replace("{" + param["name"] + "}", str(value))
    return base_url.rstrip("/") + path


def request_body_example(operation, doc):
    request_body = operation.get("requestBody")
    if not request_body:
        return None
    media = request_body.get("content", {}).get("application/json")
    if not media:
        return None
    if "example" in media:
        return media["example"]
    examples = media.get("examples")
    if isinstance(examples, dict) and examples:
        first = next(iter(examples.values()))
        if isinstance(first, dict) and "value" in first:
            return first["value"]
    # FastAPI/pydantic commonly emit examples on the schema itself (OpenAPI 3.1
    # JSON Schema `examples` keyword) rather than on the media type object.
    value, found = example_from_schema(media.get("schema"), doc)
    if found:
        return value
    return None


def resolve_security_headers(operation, doc):
    requirements = operation.get("security", doc.get("security"))
    if not requirements:
        return []
    schemes = doc.get("components", {}).get("securitySchemes", {})
    headers = []
    for scheme_name in requirements[0]:
        scheme = schemes.get(scheme_name)
        if not scheme:
            continue
        scheme_type = scheme.get("type")
        if scheme_type == "http" and scheme.get("scheme", "").lower() == "bearer":
            headers.append(("Authorization", f"Bearer {PLACEHOLDER_TOKEN}"))
        elif scheme_type == "apiKey" and scheme.get("in") == "header":
            headers.append((scheme["name"], PLACEHOLDER_TOKEN))
        # else: scheme type we don't recognize (basic, oauth2, ...) - skip it
        # rather than guessing at a header shape.
    return headers


def has_json_success_response(operation):
    for status, response in operation.get("responses", {}).items():
        if status.startswith("2") and response.get("content", {}).get("application/json"):
            return True
    return False


def build_curl_sample(method, url, headers, body):
    first_line = "curl -L"
    if method != "GET":
        first_line += f" -X {method}"
    first_line += f" {url}"
    lines = [first_line]
    for name, value in headers:
        lines.append(f"  -H '{name}: {value}'")
    if body is not None:
        lines.append("  -H 'Content-Type: application/json'")
        lines.append(f"  -d '{json.dumps(body)}'")
    return " \\\n".join(lines) + "\n"


def build_python_sample(method, url, headers, body, print_response):
    args = [f"    '{url}',"]
    if headers:
        headers_literal = "{" + ", ".join(f"'{k}': '{v}'" for k, v in headers) + "}"
        args.append(f"    headers={headers_literal},")
    if body is not None:
        args.append(f"    json={body!r},")
    args[-1] = args[-1].rstrip(",")

    call = f"{'r = ' if print_response else ''}requests.{method.lower()}("
    lines = ["import requests", call, *args, ")"]
    if print_response:
        lines.append("print(r.json())")
    return "\n".join(lines) + "\n"


def build_javascript_sample(method, url, headers, body, print_response):
    options = []
    if method != "GET":
        options.append(f"  method: '{method}',")
    fetch_headers = list(headers)
    if body is not None:
        fetch_headers.append(("Content-Type", "application/json"))
    if fetch_headers:
        headers_literal = "{ " + ", ".join(f"'{k}': '{v}'" for k, v in fetch_headers) + " }"
        options.append(f"  headers: {headers_literal},")
    if body is not None:
        options.append(f"  body: JSON.stringify({json.dumps(body)}),")

    if options:
        call = f"const response = await fetch('{url}', {{\n" + "\n".join(options) + "\n});"
    else:
        call = f"const response = await fetch('{url}');"

    lines = [call]
    if print_response:
        lines.append("const data = await response.json();")
    return "\n".join(lines) + "\n"


def apply_code_samples(doc):
    servers = doc.get("servers", [])
    base_url = servers[0]["url"] if servers else ""
    for path, path_item in doc.get("paths", {}).items():
        for method, operation in path_item.items():
            if method not in HTTP_METHODS:
                continue
            if "x-codeSamples" in operation:
                continue  # hand-authored - trust it over anything synthesized

            url = build_url(base_url, path, path_item, operation, doc)
            headers = resolve_security_headers(operation, doc)
            body = request_body_example(operation, doc)
            print_response = has_json_success_response(operation)
            method_upper = method.upper()

            operation["x-codeSamples"] = [
                {
                    "lang": "cURL",
                    "source": build_curl_sample(method_upper, url, headers, body),
                },
                {
                    "lang": "Python",
                    "source": build_python_sample(method_upper, url, headers, body, print_response),
                },
                {
                    "lang": "JavaScript",
                    "source": build_javascript_sample(method_upper, url, headers, body, print_response),
                },
            ]


def enrich(doc, content_dir):
    apply_intro(doc, content_dir)
    apply_operation_notes(doc, content_dir)
    apply_code_samples(doc)
    return doc


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True, type=Path, help="Exported OpenAPI YAML file")
    parser.add_argument("--output", required=True, type=Path, help="Where to write the enriched OpenAPI YAML")
    parser.add_argument(
        "--content-dir",
        type=Path,
        default=Path(__file__).parent / "content",
        help="Directory containing intro.md and operation-notes.yaml (default: ./content next to this script)",
    )
    args = parser.parse_args()

    if args.input.resolve() == args.output.resolve():
        parser.error("--output must be a different path than --input")

    doc = load_doc(args.input)
    enrich(doc, args.content_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    dump_doc(doc, args.output)
    print(f"Wrote enriched spec to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
