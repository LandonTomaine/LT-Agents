# Question Bank

Use this to build a question ledger after scanning the repo. Ask the questions that matter; skip questions already answered by current docs unless confirmation is still risky.

## Target And Intent

- Is this a brand-new repo, an active product, a prototype, or a legacy codebase being cleaned up?
- What outcome do you want first: audit, proposed backbone, docs only, quality gates, repo-local skills, or full approved implementation?
- Should the first pass optimize for speed, strictness, onboarding clarity, or merge safety?
- Which files or areas are off limits?
- Are there existing user changes that must be preserved or intentionally included?
- Who is the audience: solo developer, small team, client handoff, future agents, external contributors, or all of those?

## Product

- What is the product in one sentence?
- Who are the primary users and secondary users?
- What workflow would make the product unacceptable if it failed?
- What is explicitly out of scope right now?
- What is future scope but should influence architecture?
- What terms must be used consistently?
- Are there domain terms in the code that are wrong, legacy, or user-hostile?
- What are the main product surfaces: admin, public, API, worker, mobile, CLI, integrations?
- Which workflows need durable product documentation before more coding?
- Which product decisions are settled and which are still assumptions?
- What external systems are part of the user-visible product?
- What should happen when those external systems fail?
- What data lifecycle states matter: draft, active, inactive, deleted, archived, cancelled, refunded, synced, failed?
- What historical facts must be preserved even if live configuration changes?
- What permissions, roles, tenants, accounts, organizations, or boundaries exist?
- What user-facing language must differ from internal engineering language?
- What client or stakeholder review questions must stay visible?
- Should product docs include PRDs, lightweight requirements, workflows, glossary, personas, or only a high-level overview for now?

## Runtime Surfaces

- What runtime surfaces does this repo actually have: UI/web pages, API, CLI, package/library, worker/job, mobile/desktop app, migrations/data jobs, integrations, infrastructure, or something else?
- Which surfaces are current, which are planned, and which are historical or dead code?
- Does the repo have a user-facing UI today? If yes, which routes, flows, auth states, and viewports matter? If no, should UI validation be marked not applicable?
- Does the repo expose an API today? If yes, which endpoints or contracts must be smoke-checked?
- Does the repo run background jobs, scheduled tasks, queues, or data migrations that need validation?
- Are there external services, webhooks, queues, storage providers, payment systems, identity providers, or other integrations that validation must account for?

## Local Setup And Deployment Docs

- Where are local setup and run instructions documented today, if anywhere?
- Are those docs complete enough for a new human or agent to run the repo without guessing?
- What prerequisites, tool versions, package managers, SDKs, databases, services, containers, or emulators are required?
- What install, restore, build, and local run commands are canonical?
- What local URLs, ports, endpoints, CLI commands, workers, or dashboards should be documented?
- What env vars, local config files, secrets, test accounts, seed data, or fixtures are required?
- Which setup or run steps are unsafe, slow, paid, external-service-dependent, or require approval?
- Does this repo deploy, release, publish a package, provide infrastructure, or have no deployable artifact?
- Where are deployment, release, or publish instructions documented today, if anywhere?
- What environments exist: preview, dev, test, staging, production, customer sandbox, package registry, app store, or none?
- Who is allowed to deploy, release, or publish? May Codex ever do it?
- Is deployment driven by a command, CI pipeline, provider dashboard, manual checklist, or external team?
- What config, secrets, feature flags, generated assets, migrations, approvals, or release notes are required?
- What post-deploy smoke checks, logs, metrics, traces, alerts, or job dashboards must be checked?
- What rollback, stop condition, or escalation rule should be documented?
- If local setup or deployment docs are missing, should the bootstrapper create focused docs, update an existing README/doc, or defer with an owner?

## Architecture

- What architectural style is intended: layered, vertical slice, modular monolith, microservice, event-driven, clean architecture, MVC, feature folders, package-by-domain, or something else?
- Which modules/layers may depend on which other modules/layers?
- Which dependencies are forbidden in core/domain/business logic?
- What is the transaction boundary?
- Where should business rules live?
- Where should validation live?
- Where should authorization live?
- Where should external integrations live?
- Where should mapping/DTO/contracts live?
- Are repositories, services, handlers, controllers, jobs, or use cases the primary application boundary?
- Which existing patterns are intentional and which are accidental?
- What conventions should architecture tests enforce?
- What exceptions are legitimate, and how should they be documented?
- Are there generated files, migrations, or vendored code that need analyzer exceptions?
- What areas are too unstable for strict architecture tests yet?

## Backend Standards

- Which language/framework versions are canonical?
- How are dependencies managed and updated?
- What formatter and analyzer rules should be authoritative?
- Should warnings fail builds? Locally, in hooks, in CI, or later?
- What naming conventions matter beyond language defaults?
- What error-handling style is preferred?
- What logging/telemetry rules matter?
- What async/cancellation/resource cleanup rules matter?
- What database access patterns are allowed or forbidden?
- How should migrations be created, reviewed, and validated?
- What comments are useful, and what comments should agents avoid?

## Frontend Standards

- What frontend surfaces exist?
- What framework or rendering model is intended?
- Where should browser behavior live?
- Are inline scripts, inline styles, or inline event handlers allowed?
- What lint, type-check, style, formatting, accessibility, and generated-asset checks should run?
- What responsive viewports must be validated?
- What design system or CSS organization should be protected?
- Where should API clients, page scripts, components, partials, and shared helpers live?
- What should agents manually verify in a browser before completion?

## Testing And Validation

- What test layers exist today?
- Which layer should be the default for business behavior?
- Which changes require unit, integration, contract, architecture, E2E, visual, performance, or manual checks?
- Which tests are fast enough for local hooks?
- Which tests are slow and should be explicit?
- What command proves a normal change is ready?
- What command proves a release or PR is ready?
- What validation should be required before agents call work complete?
- Are there flaky tests, environment dependencies, or credentials that change validation expectations?

## Local Validation

- How does Codex install dependencies and run the app/service locally?
- What local command or command sequence proves a normal change is ready?
- Which local checks are required by change type: backend, frontend, API, migration, integration, docs-only, config-only, or dependency-only?
- What local URLs, ports, API calls, CLI invocations, jobs, queues, scripts, or generated outputs should be exercised?
- What local services, containers, emulators, seed data, test accounts, env vars, or secrets are required?
- Which local checks may Codex run automatically, and which require explicit approval because they are slow, expensive, destructive, or credential-gated?
- What exact evidence should Codex report after local validation?

## Deployed Validation

- Does this repo have deployed environments: preview, dev, test, staging, production, customer sandbox, or none?
- Who deploys to each environment, and is Codex allowed to deploy or only validate after someone else deploys?
- What deployed URLs, endpoints, dashboards, logs, metrics, traces, monitors, job status pages, or health checks matter?
- What smoke checks are safe in each deployed environment?
- What test account, tenant, fixture, feature flag, or sample data may be used in deployed validation?
- What actions are forbidden in production or shared environments?
- What rollback, stop condition, or escalation rule should be documented?
- If deployed validation is not decided yet, may this be explicitly deferred? Who owns the follow-up?

## Tooling, Hooks, And CI

- What package managers and lockfiles are canonical?
- What commands install, build, lint, format, test, run, and generate assets?
- Should local hooks exist? Which ones: pre-commit, pre-push, commit-msg?
- Which hook tasks should block local work?
- What should CI enforce for merge protection?
- Should local hooks and CI mirror each other exactly or differ by speed?
- What generated files must stay clean after build?
- What dependency, license, vulnerability, or secret scans are required?
- What commands are unsafe or expensive and need explicit approval?

## Documentation And Agent Routing

- Should `AGENTS.md` be tiny and route elsewhere?
- What belongs in shared human docs versus agent-only rules?
- Which docs should agents always load?
- Which docs should be loaded only for backend, frontend, product, architecture, testing, or workflow tasks?
- What docs are stale, duplicated, too verbose, or missing?
- Should docs include an explicit maintenance guide?
- Which changes require documentation updates: product behavior, commands, setup, deployment, validation, architecture, API contracts, UI flows, migrations, integrations, or standards?
- Should agents update docs in the same change, propose docs updates separately, or ask before touching docs?
- Which docs are authoritative, and which are historical planning artifacts or examples?
- How should stale, duplicated, or conflicting docs be handled?
- What docs should never be overwritten without explicit review?
- Should PR/review guidance require checking related docs?
- Should this repo have a repo-local `update-documentation` skill? It would update or propose updates to human docs and agent routes when code, commands, product behavior, architecture, validation, deployment, or standards change.
- If an `update-documentation` skill is useful, should it be repo-local, user/global, ignored, or deferred?
- Should the repo include a non-product standards adoption TODO/roadmap for deferred linters, architecture tests, CI/hooks, dependency/security checks, validation docs, deployment docs, docs maintenance, or skill migration?
- If yes, should it live at `docs/development/standards-roadmap.md`, inside an existing tracker, or somewhere else?
- How should unresolved questions be tracked?
- Should indexes be routing tables only, with policies in focused files?
- Are there current docs that humans use and agents should not overwrite without review?

## Repo-Local Skills

- What repeated repo workflows should become skills?
- Which existing global skills already cover the need?
- Which workflows are better as short shared docs instead of skills?
- Should skills be repo-local under `.agents/skills` or global under `$HOME/.agents/skills`?
- If legacy `.codex/skills` exists, should it be kept, migrated to `.agents/skills`, or supported temporarily?
- `audit-skills` reviews skills for trigger quality, brevity, DRYness, and resource placement. Should it be repo-local, user/global, ignored, or deferred for this repo?
- `improve-ai-self` analyzes repeated agent failures or bad assumptions and turns them into updated guidance, skills, scripts, or docs. Should it be repo-local, user/global, ignored, or deferred for this repo?
- `update-documentation` updates or proposes updates to repo docs and agent routes when code, commands, product behavior, architecture, validation, deployment, or standards change. Should it be repo-local, user/global, ignored, or deferred for this repo?
- Which validation skills, if any, match confirmed repo surfaces: UI/browser, API smoke, CLI validation, worker/job validation, migration validation, deployed smoke validation, or none?
- If the repo has no confirmed UI, should UI/browser validation be rejected as not applicable?
- What should each skill trigger on?
- What should each skill refuse or ask before doing?
- What references or scripts would keep each skill short?
- Should skills create durable files, or only draft for approval?
- Which skill outputs should be concise plans, reviews, changed files, or validation reports?

## Process

- What branch naming, commit, PR, and review conventions should be documented?
- Should agents create commits or PRs by default, only when asked, or by workflow?
- What is the expected handoff format?
- How is work tracked: file-based PRDs/backlogs, GitHub, Azure DevOps, Linear, Jira, another tracker, or no durable tracker?
- If an external tracker is used, should the repo have only a generic `docs/development/work-tracking.md` TODO until the workflow is confirmed?
- If file-based planning is used, should this repo include example PRD/backlog files or only indexes?
- What must never be done without approval?
- What does "done" mean for this repo?
- When is this standards-bootstrap pass allowed to stop if questions remain?

## Adoption And Tradeoffs

- Which gaps should be fixed now?
- Which gaps should be documented but deferred?
- Which strict checks would create too much churn today?
- Is the repo allowed to have temporary exceptions? Where should they live?
- Should the first implementation batch be docs-only?
- Should quality gates be added in warn-only mode first?
- What would make this standards system too heavy for the repo size?
