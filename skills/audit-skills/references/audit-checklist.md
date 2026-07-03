# Audit Checklist

Use only the sections relevant to the current audit.

## Trigger Quality

- Does the frontmatter description clearly say what the skill does?
- Does it clearly say when to use it?
- Should the skill be explicit-only instead of inferred?
- Does the description overclaim or match too many unrelated requests?

## DRYness

- Does `SKILL.md` repeat agent rules that are already always loaded?
- Does it repeat repo-specific guidance that should stay in repo docs?
- Does it repeat information already present in nearby `references/` or `scripts/`?
- Are there duplicated examples or near-duplicate sections that could collapse into one rule?

## Brevity

- Is every paragraph earning its place?
- Can long lists compress into a smaller checklist?
- Are there examples that teach nothing new?
- Are there template leftovers, filler headings, or generic scaffolding text?

## Progressive Disclosure

- Does `SKILL.md` keep only the core workflow and decision rules?
- Should detailed examples, checklists, or domain notes move into `references/`?
- Should repeatable commands or deterministic helpers move into `scripts/`?
- Are references one level deep and clearly linked from `SKILL.md`?

## Resource Placement

- Is there skill-specific detail that belongs in nearby resource files instead of the main body?
- Are there scripts that should exist because the same command sequence or helper logic keeps being rewritten?
- Are there references that are specific to the skill instead of broad repo docs?
- Is the skill creating extra files that do not help execution?

## Output Discipline

- Does the skill tell the agent what to return, or does it leave the output shape vague?
- Does the requested output match the actual workflow?
- If the skill mentions severity, blocking status, or conclusions, are those reflected consistently in the output format?
