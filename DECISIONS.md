# Decisions

Three lines per decision: what I chose, what I rejected, why. Add "Revisit if" only when there is a clear trigger.

### D-001 Track work in plain markdown (ROADMAP, DECISIONS, specs/, TIMELOG)
Chose: markdown files in the repo. Rejected: issue tracker, README only.
Why: zero tooling, versioned with the code.


### D-002 Environment setup [specs/000-environment-setup.md](specs/000-environment-setup.md)
Chose: 
- python 3.12
- uv
- pytest
- mypy
- ruff 

Rejected:
 - python 3.13+: no reason, 3.12 is stable 
 - pip +venv , cause uv streamline both into single excutable


Why: 
- python 3.12, stable
- uv, rust based package manager, venv
- pytest: testing
- mypy: static type checking
- ruff : format and linting