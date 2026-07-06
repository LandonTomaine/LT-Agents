# Validation Decisions

Load when asking, resolving, or proposing testing, local validation, deployed validation, smoke checks, or validation skills.

## Policy

- Separate tests from validation. Tests are executable checks by layer; validation is the proof that a change works in the relevant local and deployed contexts.
- Do not assume a UI exists. Confirm repo surfaces from evidence and the user before proposing UI/browser validation.
- Do not assume deployed validation exists. Ask whether there are preview, dev, staging, production, or customer environments and what Codex may safely touch.
- Do not accept vague answers like "run the tests" or "check the site" as complete validation policy.
- If the user wants to decide later, record `defer` with owner, trigger, and next step. Otherwise keep asking.

## Surface Inventory

For each target repo, classify the runtime surfaces before proposing skills or docs:

- UI/web pages
- HTTP API
- CLI
- library/package
- background worker, queue consumer, scheduled job, or daemon
- mobile/desktop app
- database migrations or data jobs
- external integrations
- infrastructure/deployment-only repo

Each confirmed surface needs:

- local setup and run command
- local validation command or manual check
- required env vars, secrets, seed data, test accounts, or fixtures
- expected pass signal
- known flaky, slow, unsafe, or credential-gated checks
- deployed validation answer when deployed environments exist

## Local Validation Questions

Ask enough to make the completion rule executable:

- What command proves a normal change is ready locally?
- Which checks are required by change type: backend, frontend, API contract, database, migration, integration, docs-only, config-only?
- How does Codex run the app or service locally?
- What local URLs, ports, routes, commands, jobs, queues, or scripts should be exercised?
- What seed data, test accounts, env vars, services, containers, or emulators are needed?
- Which checks are fast enough for every task, and which are explicit because they are slow or costly?
- What local evidence should Codex report: command output, screenshot, API response, logs, test summary, or manual result?

## Deployed Validation Questions

Ask separately for every environment that exists:

- What environments exist: preview, dev, test, staging, production, customer sandbox, or none?
- Who can deploy to each environment, and should Codex ever deploy?
- What URL, app, API endpoint, job dashboard, logs, or monitor proves the deployed change works?
- What test account, tenant, fixture, feature flag, or safe data may be used?
- What actions are forbidden in production or shared environments?
- What smoke checks are required after deploy?
- What logs, metrics, alerts, traces, or background job status should be checked?
- What rollback or stop condition should be documented?

## Docs To Propose

Prefer shared docs over skills for baseline expectations:

- `docs/development/local-setup.md`: how to install, configure, and run locally.
- `docs/development/deployment.md`: how deploy, release, or publish works and who owns it.
- `docs/development/testing/strategy.md`: test layers, when to use each layer, and test commands.
- `docs/development/validation.md`: local and deployed validation matrix, environment rules, smoke checks, manual checks, credentials/test-data assumptions, and completion proof.

Use `references/operational-docs.md` before proposing local setup or deployment docs. Do not merge all setup, deploy, testing, and validation policy into one large file unless the repo is tiny and the user approves that shape.

Use a TODO placeholder only if the user explicitly defers validation details and approves the file. Never put validation TODOs in always-loaded agent files.

## Skill Decisions

Create or tailor a validation skill only when the workflow is repo-specific, repeated, and more complex than a short doc route.

Ask placement and scope before proposing:

- UI/browser validation: only when a UI exists and routes/auth/viewports/manual checks are known or explicitly deferred.
- API smoke validation: when API calls, auth, fixtures, or response assertions repeat across work.
- CLI validation: when command invocations, fixtures, exit-code checks, or generated outputs repeat.
- Worker/job validation: when queues, schedulers, logs, dashboards, or side effects need a repeatable check flow.
- Deployed smoke validation: when the repo has known environments and safe post-deploy checks.

If the repo has no confirmed UI, mark UI/browser validation as rejected or not applicable. Do not scaffold a placeholder UI validation skill.

Use `scripts/scaffold_backbone.py <repo> --mode draft --set ui-validation-skill` only after UI/browser validation is approved. The generated skill is a starter; tailor it to the repo's run command, browser surface, auth/test data, artifact rules, and cleanup expectations before applying or treating it as authoritative.

## Manifest Requirements

Every proposed validation item must include:

- path or skill name
- local/deployed scope
- surfaces covered
- create/update/skip/defer action
- required commands or manual checks
- unresolved questions, if explicitly deferred
- whether Codex may run it automatically or must ask first
