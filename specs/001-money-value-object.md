# 001: Money value object

- Status: In Progress
- Phase: 1
- Started / finished: Started
- New dependencies introduced (and why): none expected (stdlib only)

## Goal
A `Money` type that cannot be misused: exact arithmetic, currency-safe, immutable.

## Concepts to research
- `decimal.Decimal`, context, rounding modes, why strings not floats in constructors
- Value object vs entity
- `dataclass(frozen=True)`, `__eq__`, `__hash__`
- Operator overloading and when to return `NotImplemented`
- Currency minor units (JPY has 0 decimals, BHD has 3)

## Design


## Acceptance criteria
- [ ] Equal amounts and currency compare equal and hash equal
- [ ] Adding different currencies is rejected with a domain error
- [ ] Rounding rule is explicit and documented
- [ ] Instances are immutable
- [ ] Fully type-hinted and passes the type checker

## Test plan
(You list the tests first. Think about: zero, negative, huge values, rounding boundaries, mixed currency, equality and hashing in sets and dict keys.)

## Instructor questions
| Question | Your answer | Follow-up |
|----------|-------------|-----------|
| Should Money allow negative amounts? Who decides, Money or Account? | | |
| Where does rounding happen, and who owns the rounding policy? | | |
| Is multiplying Money by Money meaningful? What about Money by a number? | | |
| Why is a value object compared by value but an Account by identity? | | |

## Out of scope
Currency conversion, persistence, formatting for display.

## Retrospective
