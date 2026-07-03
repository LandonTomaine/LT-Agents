# Placeholders

Load before proposing placeholder files.

## Policy

- Placeholders are allowed only in non-always-loaded docs.
- Do not put TODO placeholders in `AGENTS.md`, always-load agent files, or any file the agent must read on every task.
- Do not create placeholders to fill a folder tree.
- Create a placeholder only when the file almost certainly matters and the repo owner is expected to fill it later.
- Mark every placeholder in the manifest as `create placeholder` or `update placeholder`.
- If details are known and confirmed, write real content instead of a placeholder.

## Default Shape

Use the shortest approved shape unless the user asks for prompts or sections:

```md
# <Title>

TODO: Fill this in after the repo owner confirms the decisions needed for this repo.
```

