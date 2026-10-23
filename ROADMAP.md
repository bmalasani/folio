# Folio Roadmap

Project: a mini order-and-ledger platform, built incrementally to master Python, OOP, FP, design patterns, HTTP/gRPC, Postgres, migrations, OpenAPI and microservice patterns.

Rules:
- One new dependency or tool per step, justified in `DECISIONS.md` before install.
- Every step has a spec in `specs/`, tests written first, and green tests before commit.
- Instructor asks and reviews. Learner writes all code and overrules with a defended reason.
- Time is tracked in `TIMELOG.md` (check-in / check-out).

Status legend: [ ] todo, [~] in progress, [x] done

## Python skills to learn along the way
Each is tied to the phase where it is first needed. Tick when you can explain and use it without notes.

- [ ] Type hints, `Protocol`, `TypedDict`, generics (Phase 1)
- [ ] `dataclasses` (frozen, slots, `field`), `enum` (Phase 1)
- [ ] `decimal` and money pitfalls (Phase 1)
- [ ] Exceptions and custom exception hierarchies (Phase 1)
- [ ] Dunder methods: `__eq__`, `__hash__`, `__repr__`, `__lt__` (Phase 1)
- [ ] Context managers (`with`, `contextlib`) (Phase 2/3)
- [ ] Decorators, closures, `functools` (`partial`, `wraps`, `lru_cache`) (Phase 2)
- [ ] Iterators, generators, `itertools` (Phase 2)
- [ ] Comprehensions and immutability habits (Phase 2)
- [ ] Packaging, imports, `pyproject.toml` (Phase 0)
- [ ] `pytest` fixtures, parametrize, fakes vs mocks (Phase 0 onward)
- [ ] `asyncio`: tasks, gather, cancellation, timeouts (Phase 6)
- [ ] Concurrency model: GIL, threads vs processes vs async (Phase 6)
- [ ] Logging and config management (Phase 4/8)

## Phases

### Phase 0: Setup
- [ ] 000 Environment, repo layout, tooling, test runner, lint, type check

### Phase 1: Domain core (stdlib only)
- [ ] 001 Money value object
- [ ] 002 Account and ledger entries (double-entry invariants)
- [ ] 003 Instrument and Order entities
- [ ] 004 Domain exceptions and invariants

### Phase 2: Functional programming and patterns
- [ ] 005 Fee engine (Strategy, pure functions)
- [ ] 006 Order state machine (State pattern)
- [ ] 007 Validation pipeline (function composition)
- [ ] 008 Property-based tests

### Phase 3: Persistence
- [ ] 009 Repository interface and in-memory fake
- [ ] 010 Postgres via Docker, schema design
- [ ] 011 Migrations
- [ ] 012 Postgres repositories and Unit of Work
- [ ] 013 Transactions, isolation levels, optimistic locking

### Phase 4: HTTP API and OpenAPI
- [ ] 014 Service layer (use cases)
- [ ] 015 REST endpoints, validation, error mapping
- [ ] 016 OpenAPI contract, review and refine
- [ ] 017 Config, logging, health checks

### Phase 5: Split services and gRPC
- [ ] 018 Extract pricing service, proto design
- [ ] 019 gRPC unary and streaming
- [ ] 020 Extract accounts service
- [ ] 021 Service discovery and config between services

### Phase 6: Async, events, sagas
- [ ] 022 Domain events
- [ ] 023 Outbox pattern
- [ ] 024 Broker and consumer (notifications service)
- [ ] 025 Order placement saga with compensation
- [ ] 026 Idempotent consumers

### Phase 7: Resilience and security
- [ ] 027 Timeouts, retries, backoff
- [ ] 028 Circuit breaker
- [ ] 029 Idempotency keys on the API
- [ ] 030 Authentication and authorization
- [ ] 031 Rate limiting

### Phase 8: Observability and infra
- [ ] 032 Structured logging and correlation IDs
- [ ] 033 Metrics and tracing
- [ ] 034 docker compose for all services
- [ ] 035 CI pipeline
- [ ] 036 Kubernetes-lite deploy (optional)

### Phase 9: Hardening
- [ ] 037 Contract tests between services
- [ ] 038 Load test and profiling
- [ ] 039 Architecture review and retrospective

## Daily block loop (90 min)
1. Research 15-20 min (no copy-paste, compare options)
2. Discuss design 10 min
3. Write failing tests 20 min
4. Implement 30 min
5. Refactor and review 10 min
Break 15-20 min between blocks.
