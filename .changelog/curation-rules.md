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

## Notes

- Exclusions apply to the public, customer-facing changelog only — they do not
  change what Zeta reports internally.
