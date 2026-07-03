# Operational Docs

Load when asking, resolving, or proposing docs for local setup, local run, environments, deployment, release, or package publishing.

## Policy

- Find existing docs first. Do not create duplicate setup or deployment docs if `README.md`, `CONTRIBUTING.md`, `docs/`, or provider docs already cover the need clearly.
- If existing docs are partial, propose targeted updates and route to them from indexes.
- If no adequate docs exist, propose focused non-always-loaded docs.
- If deployment, release, or publish does not apply, document the decision or record it as rejected/not applicable.
- If the user defers details, record `defer` with owner and next step.

## Where To Look

Inspect likely files and search terms:

- Files: `README*`, `CONTRIBUTING*`, `docs/**`, `.github/workflows/**`, `azure-pipelines.yml`, `.gitlab-ci.yml`, `Jenkinsfile`, `Dockerfile`, compose files, `Procfile`, provider config, `wrangler.toml`, Cloudflare config, `supabase/**`, `deploy/**`, `deployment/**`, `infra/**`, `infrastructure/**`, `k8s/**`, `helm/**`.
- Local terms: `getting started`, `setup`, `install`, `restore`, `run locally`, `local`, `dev server`, `localhost`, `ports`, `environment variables`, `secrets`, `seed`, `fixture`, `docker compose`, `emulator`.
- Deploy terms: `deploy`, `deployment`, `release`, `publish`, `preview`, `staging`, `production`, `environment`, `pipeline`, `migration`, `rollback`, `smoke`, `health check`, `Cloudflare`, `Supabase`, `wrangler`.

## Adequate Local Setup Docs

Local setup/run guidance is adequate only when a new human or agent can identify:

- prerequisites and tool versions
- dependency install/restore command
- required environment variables, secrets, or local config files
- required local services, containers, emulators, or databases
- data setup, seed, fixture, or test account requirements
- command to run each relevant app/service/surface locally
- local URLs, ports, endpoints, CLI commands, or other entrypoints
- command or observation that proves the app/service started correctly
- known slow, unsafe, paid, external, or credential-gated steps

## Adequate Deployment Or Release Docs

Deployment/release guidance is adequate only when the repo owner can identify:

- whether this repo deploys, releases, publishes, or has no deployable artifact
- environments: preview, dev, test, staging, production, customer sandbox, package registry, app store, or none
- who is allowed to deploy/release and whether Codex may do it
- deploy/release trigger: command, CI pipeline, manual checklist, provider dashboard, or external process
- required secrets, config, feature flags, migrations, generated assets, or approvals
- post-deploy smoke checks and where to see logs, metrics, traces, alerts, or job status
- rollback, stop condition, or escalation rule
- production/shared-environment actions that are forbidden

## Docs To Propose

Prefer existing docs when adequate. Otherwise use these defaults:

- `docs/development/local-setup.md`: local prerequisites, install, env/secrets, local services, run commands, URLs, data setup, and troubleshooting.
- `docs/development/deployment.md`: environments, deploy/release/publish ownership, commands or pipelines, config/secrets, migrations, smoke checks, rollback/stop rules, and access constraints.

For tiny repos, a short `README.md` section may be enough. For larger repos, keep `README.md` as an entrypoint and put details in focused docs.

## Manifest Requirements

Every proposed operational doc item must include:

- path
- create/update/skip/defer/not-applicable
- existing docs found, if any
- local setup/run or deployment/release scope
- known commands or owners
- unresolved questions, if explicitly deferred
- routes/indexes that must be updated with it
