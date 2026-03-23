# Guardian v0.2 — Decision Equivalence

## Status
Draft

## Core Definition

Two decisions A and B are equivalent iff their invariant boundaries
are identical under the same identity context.

## Notes

- Independent of transport / encoding / envelope
- Deterministic and verifiable

=======

## 1. Scope

This specification defines when two decisions are equivalent.

It does not define:
- whether a decision is authorized
- whether a decision should be accepted
- whether a decision may be executed
- runtime transport, relay, or envelope requirements

Equivalence is a semantic relation over decisions, not an execution format.

## 2. Identity Context

Identity context defines the origin under which a decision is interpreted.

An identity context may include:
- DID
- public key
- sender identity
- credential references
- system-specific identity metadata

For equivalence, identity context is part of the invariant comparison boundary.

## 3. Invariant Boundary

The invariant boundary is the minimal set of decision properties that must remain unchanged.

Invariant boundary includes:
- decision meaning
- policy-relevant fields
- identity context
- committed semantic content

Invariant boundary excludes:
- transport-specific metadata
- encoding-specific representation
- envelope-specific fields
- relay-specific routing details

## 4. Equivalence Rule

Two decisions A and B are equivalent iff:

1. identity_context(A) == identity_context(B)
2. invariant_boundary(A) == invariant_boundary(B)
3. no invariant violation is introduced

Equivalence is strict and deterministic.

## 5. Envelope Independence

Decision equivalence is independent of:
- transport protocol
- envelope format
- encoding format (JSON, CBOR, etc.)
- field ordering

## 6. Normalization

Before comparison:
- decode representation
- remove transport-specific fields
- canonicalize structure
- resolve identity context

Normalization must not change semantic meaning.

## 7. Verification Procedure

1. Parse A and B
2. Normalize identity context
3. Normalize both decisions
4. Extract invariant boundary
5. Compare invariant content
6. Return equivalent / not equivalent

## 8. Minimal Reference Implementation

```python
def verify_equivalence(a, b):
    if normalize_identity(a) != normalize_identity(b):
        return False

    if extract_invariant(a) != extract_invariant(b):
        return False

    return True
```
## 9. Examples

Equivalent:
- JSON vs CBOR encoding
- different envelopes

Not equivalent:
- different policy meaning
- different identity context

## 10. Counterexamples

The following do NOT imply equivalence:
- both verify cryptographically
- both execute successfully
- both bind to valid entities

## 11. Subsumption

Any system comparing decisions defines an implicit equivalence relation.

This specification makes it explicit.

## 12. Boundary to Acceptance

Equivalence does not imply acceptance.

Acceptance is defined in Guardian v0.3.
>>>>>>> 9e0f2ab (docs: formalize Guardian v0.2 decision equivalence spec)
