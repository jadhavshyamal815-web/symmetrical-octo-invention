# MDU — Evidence Provenance and Schema Discipline

## Role

MDU supports evidence provenance, source lineage, terminology discipline and schema consistency within the research-evidence workflow.

MDU does not independently approve scientific claims, formulations, clinical conclusions or regulatory decisions.

## Evidence Provenance

Each evidence record should retain a traceable relationship between:

Source
→ Source ID
→ Evidence ID
→ Claim ID
→ Evidence type
→ Evidence strength
→ Limitations
→ Contradiction status

This structure allows reviewers to identify where a statement originated and how its confidence was classified.

## Source Lineage

The source register is the primary reference point for source identity.

Evidence records should not rely on unidentified references or unsupported summaries.

Where possible, source records should retain:

- source_id
- source title
- source type
- organization or journal
- publication information
- public source location
- verification status
- provenance notes

## Terminology Discipline

The framework distinguishes:

- Traditional knowledge
- Research hypothesis
- Preclinical evidence
- Human evidence
- Systematic review
- Meta-analysis
- Contradictory evidence
- Evidence limitation
- Translation gap

These terms must not be treated as interchangeable.

Historical use does not automatically establish efficacy.

Preclinical findings do not automatically establish clinical relevance.

Scientific evidence does not automatically establish product approval.

## Schema Discipline

The reusable evidence schema is maintained in:

`evidence_framework/evidence_schema.json`

Structured records should follow the defined fields and retain provenance information.

Changes to the schema should be documented rather than silently altering the meaning of existing records.

## Contradiction Discipline

Contradictory findings must remain visible.

The contradiction register should identify:

- contradiction_id
- related claim_id
- relevant evidence
- contradiction description
- resolution status
- reviewer/provenance note

Contradictions should not be removed simply because they complicate interpretation.

If a claim is downgraded, the reason for the downgrade should remain traceable.

## Unknowns

Unknown or unavailable information must remain explicitly unknown.

The framework must not fill missing evidence with assumptions, generated citations or unsupported interpretation.

## Current Status

- Source provenance structure: Implemented
- Evidence schema: Implemented
- Claim linkage: Implemented
- Contradiction register: Implemented
- Evidence-strength classification: Implemented
- Structured JSON output: Implemented
- Final provenance review: Pending

## Quality Principle

The evidence system should make it possible for another researcher to trace a statement backward from:

Translation question
→ claim
→ evidence record
→ source
→ provenance information

without depending on undocumented personal interpretation.