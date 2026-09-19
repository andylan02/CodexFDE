# Issue tracker: GitHub

Issues and specs for this repo live in the GitHub repository for `andylan02/CodexFDE`. Use the `gh` CLI for all issue operations.

## Conventions

- Create an issue: `gh issue create --title "..." --body "..."`
- Read an issue: `gh issue view <number> --comments`
- List issues: `gh issue list --state open --json number,title,body,labels`
- Comment on an issue: `gh issue comment <number> --body "..."`
- Apply or remove labels: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- Close an issue: `gh issue close <number> --comment "..."`

Infer the repo from `git remote -v`; `gh` picks it up automatically inside the workspace clone.

## Pull requests as a triage surface

PRs as a request surface: no.

This repo treats issues as the main triage surface. If PRs are later used as feature requests, the `triage` skill can flip this later, but the default setup keeps external PRs out of the queue.

## When a skill says "publish to the issue tracker"

Create a GitHub issue in this repository.

## When a skill says "fetch the relevant ticket"

Run `gh issue view <number> --comments`.

## Wayfinding operations

Use a single issue as the map and child issues as tasks. Keep blockers visible in the issue metadata and in the map body rather than burying them in side documents.
