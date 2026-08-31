# DEP Metadata

## Task Identity

- Task: Scientific Evidence and Translational Research Mapping
- Test Task: 2 of 7-4-3
- Owner: Shyamal
- Division: BHIV Biotech
- State: WORKING
- Convergence Status: PARTIALLY CONVERGED

## Scope

Build a scientifically traceable research-evidence workflow around one non-sensitive public-domain botanical or biological concept using publicly available scientific and regulatory sources.

## Selected Demonstration Concept

- Concept: Curcuma longa L. (turmeric/curcumin)
- Research context: Evidence mapping related to curcumin and osteoarthritis
- Classification: Non-sensitive public-domain botanical research concept

## Evidence Boundaries

The framework separates:

- Traditional knowledge
- Research hypotheses
- In vitro evidence
- In vivo evidence
- Human evidence
- Systematic reviews and meta-analyses
- Contradictory evidence
- Evidence limitations
- Translation gaps

Historical or traditional use is not treated as proof of scientific efficacy.

## Non-Goals

This task does not establish:

- Medical advice
- Patient treatment recommendations
- Clinical efficacy
- Safety approval
- Regulatory approval
- Manufacturing suitability
- Commercial viability
- Product approval

No laboratory experimentation, clinical experimentation, controlled substances, restricted materials or cannabis-related work is included.

## Source Policy

Evidence should be based on publicly available and academically or regulatorily credible sources, including:

- PubMed
- NIH / NCCIH
- Cochrane
- WHO
- Peer-reviewed scientific journals

Blogs, marketing pages and AI-generated summaries are not used as primary scientific evidence.

## Traceability Requirements

Every evidence claim should retain:

- claim_id
- source_id
- evidence_type
- evidence_strength
- limitations
- contradiction_status
- provenance_note

Source provenance and evidence versioning must remain visible.

## Contradiction Policy

Contradictory or weak evidence must not be silently removed or resolved.

Where evidence is insufficient, the framework must:

1. Preserve the original record.
2. Record the limitation.
3. Record contradiction status where applicable.
4. Downgrade unsupported claims where justified.
5. Preserve unknown information as unknown.

## Current Implementation Status

Completed:

- Reusable evidence framework
- Evidence schema
- Source register
- Evidence map
- Claim traceability map
- Contradiction register
- Translation-gap register
- Python evidence tracker
- Sample evidence record
- Structured JSON output
- Review packet

Pending:

- Final DEP review
- Screenshot evidence packaging
- Final quality-control review
- Final handover preparation

## Known Unknowns

- Final Test Task 1 evaluation status
- Exact source-pack availability
- Whether additional reviewer-specific evidence requirements will be requested

## Verification

Last verified:

Current task execution

Verification principle:

Public source → source registration → evidence classification → claim linkage → contradiction detection → translation-gap identification → future R&D decision input.