# Curation rules — Zenlytic Release Notes

Every run must read this file and apply these rules before drafting. These are
standing exclusions on top of the base spec (which already drops internal
refactors, tests, CI/CD, infra, dependency bumps, and no-impact changes).

## Hard exclusions (never publish)

- **VPC** — Anything related to VPC / customer VPC deployments. Drop the item
  entirely; do not reword or generalize it. If a day's only change is VPC, that
  day produces no entry. Also state this exclusion in the Zeta request so Zeta
  omits VPC changes up front.

- **Custom SAML/SSO connections** — Changes to custom SAML/SSO connection
  handling (token lifetimes, redirect behavior, connection setup, etc.) only
  affect in-VPC customers, even when the item isn't explicitly labeled VPC.
  Treat these as covered by the VPC exclusion above and drop them entirely.
  (Paul's rule, 2026-07-07. Example: "Longer SAML sessions" — a SAML
  access-token-lifetime change — was pulled from the July 6, 2026 entry
  after publishing; it only affects custom SAML connections used by
  in-VPC customers, and describing it without that context implied it
  applied to standard/non-VPC SSO too. Ask Zeta to flag custom-SAML items
  explicitly going forward so they can be excluded up front rather than
  caught in review.)

- **Don't reveal VPC-vs-SaaS infra differences or regressions** — Even for
  GA, non-VPC items: exclude (or reword to remove the tell) anything whose
  description would surface that sandbox/infra behavior differs, or once
  regressed, between in-VPC and SaaS deployments. The changelog should not
  let readers infer that the two deployment models' underlying feature sets
  diverge or that one had a bug the other didn't.
  (Paul's rule, 2026-07-13. Example: "Zoë context manager works across
  sandbox backends" was pulled from the Week of July 6–12, 2026 entry after
  publishing — the item existed because it fixed a difference in sandbox
  infrastructure between in-VPC and SaaS, and describing the fix in the
  changelog revealed that gap/regression. Ask Zeta to flag items that touch
  sandbox-backend or infra parity between VPC and SaaS explicitly going
  forward so they can be excluded or reworded up front rather than caught in
  review.)

- **GA-only — include an item ONLY if Zeta confirms it is generally available.**
  Default to exclude. An item qualifies only when Zeta confirms either no gating
  feature flag, or that the gating flag's production default/fallthrough is `on`
  for all users. If an item is behind a flag that defaults off (or to targeted
  beta), or Zeta cannot confirm GA, leave it out — do not soften or hedge.
  "Merged to master" is not enough; availability is decided by the flag's prod
  default, which Zeta reads from the source / LaunchDarkly. Ask Zeta, per change,
  for: gating flag name (if any), the flag's prod default, and a yes/no on GA.
  (Paul's rule, 2026-06-26; tightened to GA-confirmation 2026-06-26. Example:
  the `artifact-foldering` flag defaulted off in prod, so artifact folders /
  table+gallery were correctly excluded.)

- **External MCP-server / AI-client connectivity is beta — exclude until Paul
  confirms public availability.** The Zenlytic MCP server and everything that
  lets external AI clients connect to Zenlytic (OAuth login for MCP clients,
  the MCP authorization/connection screen, MCP tool capability metadata,
  multi-workspace MCP tokens) is not public or out of beta, even where Zeta
  reports no gating flag / GA-yes. Paul's ruling overrides Zeta's GA
  determination for this cluster. Items live on the held-items watchlist;
  release only on Paul's explicit confirmation, not on a flag flip alone.
  (Paul's rule, 2026-07-27. Example: "Connect AI clients to Zenlytic over
  MCP", "Improved MCP connection screen", and "Accurate MCP tool capability
  metadata" were pulled from the Week of July 20–26, 2026 entry after
  publishing.) Note: this does NOT cover in-app MCP connections used inside
  Zenlytic chat (e.g. admin defaults for chat MCP connections) — those are a
  separate, GA surface.

- **No implementation-detail items.** The changelog describes user outcomes,
  not plumbing. Exclude items whose substance is an endpoint's filter/sort
  parameters, delivery mechanics, or other technical implementation details —
  even when GA. (Paul's rule, 2026-07-27. Examples pulled from the July 20–26
  entry: "Agent list search/sort/filter API", "Shareable chats in agent
  deliveries".) These are permanent editorial exclusions — they do NOT go on
  the held-items watchlist.

- **Pre-launch fixes and polish are part of the launch.** When a feature
  reaches GA in the covered period, work that fixed or polished it BEFORE
  customers could see it is not a separate bug fix or improvement — customers
  never experienced the broken state. Fold it into the launch item or drop
  it. Only list a fix separately if the broken behavior was live for
  customers. (Paul's rule, 2026-07-27. Example: agent result-delivery,
  timezone, run-history, and display "fixes" were pre-GA polish of the
  Proactive Agents launch and were folded into the launch bullet.)

## Voice and framing (Paul, 2026-07-27)

- **Lead features with user value, not UI rework.** A launch bullet should
  say what the feature does for the user (e.g. agents that sync context via
  MCP connections and alert conditionally — only when something matters), not
  "redesigned editor and list."
- **Don't present existing capabilities as new.** If a change increases how
  often or how well an existing behavior shows up (e.g. Zoë using Markdown
  tables more often), describe it as that — not as a new capability.

## GA carve-outs (narrow segment exceptions don't block publishing)

A flag counts as GA if its production fallthrough/default serves `true` to
everyone, even if a narrow named-segment rule still serves `false` to a
specific account or org (e.g. one enterprise customer opted out, or a
Salesforce/Verizon-style segment rule). Publish the item; don't hold it for
a single-account carve-out. Only hold items where the *fallthrough itself*
is off or targeted-beta.
(Confirmed via Zeta 2026-07-01 on `artifact-foldering`: fallthrough on for
prod + prodeu, with one segment rule off for `verizon-saas-organizations`.
Treated as GA and published.)

## Flag-flip watchlist (re-check previously-held items)

Every item dropped as non-GA must be logged to `held-items.json` (open
watchlist), not just silently discarded. Each run, before doing the normal
commit-diff query, re-check every open watchlist item's flag against
LaunchDarkly's CURRENT production state via Zeta. If a flag has flipped from
off/targeted to on, the item is "recovered": publish it dated to the FLIP
date (when it became visible to users), not its original merge date, then
move it from the open watchlist to the resolved log.

**Why:** our whole workflow dedups on `cutoff_sha` — a git commit diff. A
flag flip is not a commit. `artifact-foldering` merged 2026-06-24, was
correctly excluded on 2026-06-26 (flag off), and because its commit SHA fell
behind the cutoff on every later run, it would never have been asked about
again — even after the flag flipped on 2026-07-01 — without a separate,
flag-based re-check. Caught 2026-07-01 only because Greg noticed the feature
live in the product and asked Zeta directly. [[release-notes-exclude-feature-flagged]]

**How to apply:** treat "excluded for not-GA" as a pending state, not a
terminal one. The watchlist is the mechanism that keeps pending items in
front of us until LaunchDarkly confirms GA.

## Tags — canonical vocabulary (2026-08-02)

Exactly three tag slugs, derived from the `###` subsections an entry actually
contains. Never invent one, never use cadence labels like "Weekly update".

| Subsection heading | Tag slug | Library label | Icon |
| ------------------ | -------- | ------------- | ---- |
| New features       | `new-features` | New features | rocket |
| Improvements       | `improvements` | Improvements | sparkles |
| Bug fixes          | `fixes`        | Fixes        | wrench / screwdriver |

The tag slug matches its subsection heading in every case, so the mapping is
mechanical — no translation step, nothing to remember.

The vocabulary lives in **four** places that must agree:

1. `changelog/README.md` frontmatter `tags:` — declares the filter chips
2. each `{% update %}` block's `tags=` attribute
3. the space's **Library → Tags** — sets the visible label and icon
4. this file

**Why:** change request GITBOOK-3 introduced a second spelling alongside the
first rather than replacing it, leaving 11 of 18 entries carrying both and one
carrying only a value the frontmatter no longer declared. A tag absent from the
frontmatter matches no filter chip, so those entries were silently unfilterable
— the page looked fine and the feature simply did nothing. The vocabulary then
flipped twice more while we settled on `new-features`, which is what Zenlytic
has used all along.

**How to apply:** derive tags mechanically from the subsections present. If a
tag would fall outside the three above, the entry is structured wrong — fix the
structure, not the tag.

## Links (2026-08-02)

Links to Zenlytic docs must be **absolute URLs**:

    [Pull from Remote](https://docs.zenlytic.com/data-modeling/cache-refresh)

**Why:** the changelog is its own GitBook section. A relative path such as
`../data-modeling/cache-refresh.md` does not resolve across a section boundary,
and GitBook does not error — it silently rewrites the link into a
`github.com/Zenlytic/zenlytic-docs/...` URL that 404s. The page builds, the link
looks normal, and the reader is sent off-site. Four links from the Docusaurus
migration survived this way until 2026-08-02 precisely because nothing failed.

**How to apply:** never emit a relative path from a changelog entry. Verify a
target resolves before linking it.

## Terminology (2026-08-02)

Current product names. Earlier terms are correct only when describing history.

| Use | Not |
| --- | --- |
| Proactive Agents | Workflows, Proactive Analytics |
| Context Manager  | Data Model Editor |
| Relationships    | identifiers, Topics (for new joins) |
| Skills           | Memories (for new context) |
| Artifacts        | code interpreter |

**Why:** the product renamed twice in a year, and Zeta's source data still
carries older names — several existing entries were drafted with "(Data Model
Editor)" trailing them. A changelog announcing a feature under a name the UI no
longer uses sends readers looking for something that isn't there.

**How to apply:** translate source terminology before drafting. If an item's
name is ambiguous, describe the surface the user actually sees.

## Output format (2026-08-02)

**File:** `changelog/README.md`. Nothing else in that directory.

**Never modify:**

- The YAML frontmatter — `description`, the `layout:` block, and the page-level
  `tags:` list. GitBook manages these; overwriting them resets page settings and
  breaks tag filtering.
- The H1 `# Product updates`. It is not "Changelog". It is the page title and
  drives the page URL.
- `changelog/SUMMARY.md`, which reads `* [Product updates](README.md "2026")`.
  The quoted `"2026"` is the navigation label, not part of the title.

**Only edit** inside `{% updates format="full" %}`. Add new entries at the top;
leave existing entries untouched.

Entry shape:

    {% update date="YYYY-MM-DD" tags="new-features,improvements,fixes" %}
    ## Short headline naming the most significant change

    One sentence summarizing the release.

    ### New features

    * **Feature name** — What it does and why it matters.

    ### Improvements

    * **Short label** — What changed.

    ### Bug fixes

    * **Short label** — What was fixed.
    {% endupdate %}

- `date` is the real ship date. It renders in the left gutter and drives both
  ordering and the RSS feed.
- The `##` heading is a **headline, never a date**. Not "Week of July 20–26" —
  the date already displays from the attribute, and this heading populates the
  on-page navigation and the anchor link. A date here makes the nav a column of
  dates instead of a scannable list of what shipped.
- `###` subsections are limited to New features, Improvements, Bug fixes. Omit
  any with no content.
- Bullets use `* **Bold label** — description.`
- Never create year pages such as `2025.md`. The annual rollover is a manual
  step: archive the closing year into its own page, empty this one, and change
  the `"2026"` link title.

**Why:** the page header is owned by GitBook and the entries are owned by this
pipeline, in the same file. Every incident so far came from one side
overwriting the other's half.

**How to apply:** treat everything above the `{% updates %}` line as read-only.

## Enforcement (2026-08-02)

`.github/workflows/validate-changelog.yml` checks every push and pull request
touching `changelog/`. It fails on a wrong H1, a tag outside the vocabulary,
tags that disagree with an entry's subsections, a date used as a headline, an
unexpected subsection heading, or a relative link.

**Why:** a rules file only works if it is read. CI does not rely on that — a
run that ignores these rules fails visibly instead of publishing quietly.

**How to apply:** if the check fails, fix the entry rather than the check.

## Sourcing and authority (previously only in the job prompt)

These rules governed every run but lived in the scheduled-task prompt rather
than this file. Recorded here (2026-07-31) so the repo is self-describing; the
scheduled-task prompt remains the executable spec.

- **Zeta is the sole authority for inputs.** The weekly commit list, every GA
  determination (LaunchDarkly production flag state), and the end-of-week
  cutoff SHA all come from Zeta (Slack agent in #troubleshooting-issues).
  Never compute a diff independently, never infer GA from anything but Zeta's
  answer. No Zeta reply = no entry and no state change — never a best-effort
  draft.
  **Why:** Zeta reads the product repo and LaunchDarkly directly; anything
  else is guesswork, and a guessed GA call publishes features customers can't
  see.
  **How to apply:** if Zeta doesn't answer within the polling window (~40s
  intervals, ~8 minutes), post the no-response notice to #changelog-upcoming
  (no Paul tag) and stop without advancing state — the unadvanced cutoff folds
  the week into the next run automatically.

- **Curation subtracts; it never adds.** These rules may exclude or hold items
  Zeta reported — including overriding a Zeta GA-yes (Paul's beta-MCP rule) —
  but may never add or promote an item Zeta didn't confirm.
  **Why:** keeps a single chain of evidence from commit → Zeta → entry.
  **How to apply:** if something seems missing from Zeta's list, ask Zeta;
  don't add it from memory or from the product UI.

- **The product repo's production branch is `origin/master`.** Never `dev`.
  Unrelated to the docs repo's `main`.
  **Why:** diffing the wrong branch reports unshipped work.
  **How to apply:** every Zeta diff request names `origin/master` explicitly.

- **Diff window and cutoff discipline.** Covered week = the most recent
  complete Mon–Sun. Window = state.json `cutoff_sha` → last Sunday 23:59
  America/Los_Angeles. The new cutoff is master's SHA at that instant — NOT
  current HEAD. The cutoff advances only when the week's output is actually
  delivered; every failure path stops without advancing state.
  **Why:** commits after Sunday belong to next week; advancing state on a
  failed run silently drops a week.
  **How to apply:** ask Zeta for the end-of-Sunday SHA in the same request as
  the diff; on any failure, post the notice and leave state untouched.

- **Cadence.** Mondays 05:00 America/Los_Angeles, covering the prior Mon–Sun,
  open-ended. No-change weeks still run: post the one-line notice and commit
  only the .changelog/ state advance. Never duplicate a week already present
  in changelog/README.md.

## Publishing pipeline (previously only in the job prompt)

- **Terminology:** the deliverable is the "change log" — that wording in PR
  titles, commit messages, PR bodies, and Slack.

- **Target and format.** `changelog/README.md` in Zenlytic/zenlytic-docs.
  The block syntax, tag vocabulary, heading rules, and the parts of the file
  GitBook owns are defined once in **Output format** above — follow that
  section rather than restating it here.

  What is specific to this pipeline: new blocks insert immediately after the
  `{% updates %}` line (newest first); the `date` attribute is the covered
  week's END date (the Sunday), except recovered watchlist items, which are
  dated to their flag-flip date; every existing block is preserved verbatim;
  never publish a week already present in the file.

  **Why:** format was previously specified in two places and drifted. The
  version here called for a cadence label as the tag, a date as the `##`
  heading, and a "Changelog" H1 — all three were corrected on 2026-08-02 and
  are now rejected by CI.

- **Paul's PR merge is the only publish gate.** Never merge a PR; never commit
  docs content to `main` directly. GitBook Git Sync publishes `main` to the
  docs site, so merge = publish. The sole permitted direct-to-`main` commit is
  the no-change-week state advance, which touches only `.changelog/` files.
  **Why:** human review is the last defense for everything these rules missed.
  **How to apply:** every content change rides a `changelog/*` branch and PR;
  the step-9 Slack notification must remind Paul that merging publishes.

- **File allowlist.** Only `changelog/README.md` and `.changelog/*` may be
  modified. Never `.gitbook.yaml`, `SUMMARY.md`, `book.json`, or workflows.

- **Open-PR guard.** If a `changelog/*` PR is still open, the prior week is
  unreviewed: notify Paul it's awaiting review, skip the run, and let the
  unadvanced cutoff fold the week forward. One PR in flight at a time.

- **GitHub access is MCP-connector only for the automated run.** No raw git
  or curl fallback. If MCP is unavailable or blocked: draft locally to the
  working folder, post the blocked notice (no Paul tag), stop without
  advancing state. (Interim exception while the org grant is pending: Greg
  runs a prepared push script under his own credentials; the automation
  itself still never falls back.)

- **Branch/PR conventions and evidence chain.** Branch
  `changelog/{week-start}-to-{week-end}`; commit "docs: change log — week of
  {range}". PR body carries: item counts by category, the cutoff line (old →
  new SHA), the Held (not GA) list, the Recovered list (merge + flip dates),
  any Paul-ruling requests, and permalinks to the Zeta watchlist and diff
  threads plus each published item's GA determination as Zeta reported it.
  After pushing, re-read the branch's changelog/README.md and confirm the new
  entry is present and nothing was lost; fix and recommit if not.

- **State files are the source of truth in the repo.** `.changelog/state.json`
  (`cutoff_sha`, `last_entry_date`), `held-items.json`, and this file. Read
  them from the repo each run, not from local copies. Every non-GA exclusion
  is logged to `held-items.json` `open` — never silently dropped. A markdown
  draft copy of each week's entry is also saved to the working folder.

- **Notifications.** Review channel: #changelog-upcoming. Paul is tagged ONLY
  on the PR-ready notification; no-change, Zeta-no-response, and failure
  notices go untagged. Zeta requests go to #troubleshooting-issues; watchlist
  re-checks are ONE batched message per run. The retired Notion "TEST Change
  Log" page is never written to.

- **Feedback loop.** Paul's PR feedback is applied as commits to the same
  `changelog/*` branch. When feedback establishes a new standing rule, append
  it to this file in the same commit.

## Additional voice rules

- **Security fixes: calm, factual language.** Describe security-related fixes
  the way any other fix is described — no alarming language, no urgency, no
  implication of customer exposure. (Paul's rule.)
  **Why:** alarmed wording in a public changelog reads as an incident
  disclosure and triggers unnecessary customer escalations.
  **How to apply:** state what was hardened or corrected, plainly. If
  severity context matters, it belongs in the PR body for Paul, not in the
  published entry.

- **Zenlytic voice.** Plain, direct, factual; no hype, no speed claims, no
  emojis, no hashtags. Surface tag in parentheses only when the item is not
  the web app (e.g. "(Slack)", "(API)", "(Data Model Editor)").

- **Attribute changes to their exact surface.** When a change applies to a
  specific feature area (e.g. Proactive Agent configuration), name that
  surface in the bullet — don't describe it generically as "chat" or
  "agents." (Paul, PR #143 review, 2026-08-03. Example: "Web search hidden
  when disabled" applied to Proactive Agent configuration specifically.)

- **Display-only permission fixes must say so.** When a fix hides a control
  the user could see but not actually use (the underlying behavior was
  already permission-gated), frame it explicitly as a UI/display-only fix so
  it cannot be read as having closed an access-control or security gap.
  (Paul, PR #143 review, 2026-08-03. Example: the model-editing tool toggle
  shown in Proactive Agent configuration was strictly UI — the capability
  itself was never accessible without permission.)

## Review notifications (Paul, 2026-08-03)

- **Paul's PR notification is ONE LINE.** The step-9 Slack message to Paul is
  the mention, the bold title "docs: change log — week of {range}", and the
  PR URL — nothing under it. All detail (item counts, cutoff line,
  held/recovered lists, ruling requests, evidence chain) lives in the PR body
  only, including the merging-publishes reminder, which moves to the top line
  of the PR body. This supersedes the longer step-9 content list in the
  scheduled-task prompt.

  **Why:** Paul reads the PR itself; a long Slack digest duplicates the PR
  body and gets skipped. On 2026-08-03 he stopped reading at the PR link, so
  the ruling requests in Slack went unread.

  **How to apply:** exactly: `<@UGKKW61T6> **docs: change log — week of
  {range}** {PR URL}` — then stop. Untagged notices (no-change,
  Zeta-no-response, blocked) keep their existing formats.

## Notes

- Exclusions apply to the public, customer-facing changelog only — they do not
  change what Zeta reports internally.
