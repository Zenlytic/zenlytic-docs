---
description: >-
  How customer data sent to Zenlytic's third-party LLM providers is used and how
  long those providers retain it.
---

# LLM Data Use and Retention Policy

{% hint style="danger" %}
**Draft — not approved for publication.** The provider retention periods, the legal entity name, and the contact address on this page have not been verified against Zenlytic's provider agreements or corporate records. Remove this notice only after Legal has confirmed each item flagged in the pull request that introduced this page.
{% endhint %}

**Last updated:** October 16, 2026

Zenlytic uses third-party large language model (LLM) providers to power Zoë and other AI features. This policy explains how customer data sent to those providers is used, and how long it is kept.

In this policy, "Zenlytic", "we" and "us" refer to Ex Quanta, Inc. dba Zenlytic, as defined in the [Terms of Service Agreement](terms-of-service-agreement.md).

## Training on customer data

Zenlytic will not use your Content to train any AI models, except for private AI models for your sole use, and will not use it to otherwise improve the Service. This mirrors the license you grant in [Terms of Service Agreement § 3.3](terms-of-service-agreement.md), which governs in the event of any conflict with this page.

Separately, under the commercial terms that govern our use of each provider's API, our LLM providers do not use customer prompts or outputs to train their models.

## Provider retention

| Provider | Accessed through | Stated retention |
| -------- | ---------------- | ---------------- |
| OpenAI | Direct API | Prompts and outputs may be retained in abuse monitoring logs for up to 30 days |
| Anthropic (Claude) | Google Cloud Vertex AI | Prompts and outputs may be retained for up to 30 days |
| Google (Gemini) | Google Cloud Vertex AI | Prompts and outputs may be retained for up to 30 days |

Retained data is used only to detect misuse. It is not used to train models.

Both LLM providers appear on our [Subprocessors](subprocessors.md) list — OpenAI directly, and Anthropic and Google models through Google Cloud Platform.

## Customer-controlled routing

Customers can route LLM traffic to their own LLM instance. Where a customer does so, that traffic is governed by the customer's own agreement with that provider, and the retention periods above do not apply to it. Retention, use, and deletion for customer-routed traffic are determined by the customer's provider agreement, not by this policy.

## Changes

LLM providers are subprocessors. When we engage a new subprocessor, we notify customers of the engagement and customers may object, as set out in [Data Processing Addendum § 4.1(6)](data-processing-addendum.md). Changes to this page are reflected in the **Last updated** date above.

## Contact

Questions about this policy can be sent to [support@zenlytic.com](mailto:support@zenlytic.com).
