# Decisions

Three lines per decision: what I chose, what I rejected, why. Add "Revisit if" only when there is a clear trigger.

### D-001 Track work in plain markdown (ROADMAP, DECISIONS, specs/, TIMELOG)
Chose: markdown files in the repo. Rejected: issue tracker, README only.
Why: zero tooling, versioned with the code.

### D-002 Python 3.12 ([spec 000](specs/000-environment-setup.md))
Chose: 3.12, pinned in `.python-version`. Rejected: 3.15 (newest), older than 3.12.
Why: security fixes until 2028-10 and wide library support. Cost: no newest language features.
Revisit if: a library we need drops 3.12, or 3.12 nears end of life.

### D-003 uv for packages, venv and workspace
Chose: uv. Rejected: pip + venv, Poetry.
Why: one tool covers Python install, venv, lockfile and workspaces, and it is fast. Cost: newer tool, smaller community than pip.

### D-004 `src/` layout
Chose: `src/<package>/` with tests outside it. Rejected: flat layout.
Why: code is importable only when installed, so tests exercise what we ship and not a stray folder on the path. Cost: needs an editable install.

### D-005 Monorepo with a uv workspace
Chose: one repo, services under `apps/`, shared code under `libs/`. Rejected: one repo per service.
Why: one person, easy refactors across services, one lockfile. Cost: weaker ownership boundaries; revisit if separate teams own services.

### D-006 Tooling: pytest, ruff, mypy
Chose: pytest (tests), ruff (lint and format), mypy (types), all dev-only. Rejected: unittest, flake8 + black + isort, pyright.
Why: pytest has fixtures and parametrize with less boilerplate, and ruff replaces three tools in one. Cost: mypy is slower and stricter than pyright in some cases.

### D-007 Root installs workspace members by dependency
Chose: root `pyproject.toml` depends on members with `workspace = true`, so plain `uv sync` installs them. Rejected: requiring `uv sync --all-packages`.
Why: a fresh clone works with two commands. Cost: each new service must be added to the root list.
