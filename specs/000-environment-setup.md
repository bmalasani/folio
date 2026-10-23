# 000: Environment setup

- Status:Done
- Phase: 0
- Started / finished: finished
- New dependencies introduced (and why): pytest, ruff, mypy

## Goal
A reproducible Python project where a fresh clone can run the tests with two commands.

## Concepts to research
- Python version selection and isolation per project (venv vs uv vs pyenv)
- `src/` layout vs flat layout
- `pyproject.toml` and what replaces `requirements.txt`
- Monorepo vs multi-repo for future services
- pytest discovery basics, ruff, mypy

## Design
- Python 3.12 is stable, recommended. I will choose uv, rust based, and includes venv, python isolation, workspaces
- I go with src layout, based on my research, flat layout can cause issues with direct imports. 
- I did research on pyproject.toml, which is a superset of requirements.txt, eqvilent to package.json, includes dependecies, tools, workspaces, python version etc.
- I go with monorepo, easy to maintain all the code one place, if the cross team, I recommend to go with multi repo so that easy ownership
- ruff for formating, mypy/pyright for static type chekcing and pytest for tesing. created a tests in playgroud/tests

## Acceptance criteria
- [x] Python version pinned and documented
- [x] Dependencies isolated from the system Python
- [x] One command installs; one command runs tests; one command runs lint and type check
- [x] A trivial passing test exists, and you have seen one fail on purpose
- [x] Git repository initialized with a sensible ignore file and a first commit
- [x] ROADMAP.md, DECISIONS.md, TIMELOG.md, specs/ committed
 
 Commands: uv sync, uv run pytest , uv run ruff check, uv run mypy -p playground

## Test plan
- A smoke test that proves the package imports from the test environment.
- Break it deliberately and confirm the runner reports the failure.

## Instructor questions
| Question | Your answer | Follow-up |
|----------|-------------|-----------|
| What Python version will you target, and why not newest or oldest? | 3.12 Stable and End of life still 2028-10, latest is 3.15, which may not ready for production works| |
| src/ layout or flat, and what does each protect you from? | src| |
| Which tools are needed on day one, and why is Postgres not one of them? | ruff, pytest, mypy,uv | |
| Could a teammate reproduce your environment in two commands? Show me. | git clone, uv sync, uv run pytest | |
| Why does float fail for money? What did you observe in the REPL? | > 1.11+2.03
3.1399999999999997, tried this, its because floating numbers need to store in binary and eventlyy get some error like 1/3=0.333 where as 0.333*3 never1 :P | |

## Out of scope
Docker, databases, web frameworks, CI.

## Retrospective
