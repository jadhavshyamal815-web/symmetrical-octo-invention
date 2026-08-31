# Scientific Evidence and Translational Research Mapping

## BHIV Biotech – Test Task 2 of 7-4-3

### Owner

Shyamal

### Project Status

WORKING

### Convergence Status

PARTIALLY CONVERGED

---

## 1. Purpose

This project develops a reusable scientific evidence-to-translation research framework.

The framework is designed to collect, classify, evaluate and trace publicly available scientific evidence while keeping traditional knowledge, research hypotheses, preclinical evidence, human evidence, contradictions, limitations and translation gaps distinct.

The selected demonstration concept for this implementation is:

**Curcuma longa L. (turmeric/curcumin) — evidence mapping related to knee osteoarthritis.**

The purpose is to demonstrate evidence infrastructure and scientific traceability, not to establish that the selected botanical or formulation is effective, safe, approved, manufacturable or commercially viable.

---

## 2. Scope

The project covers:

- Traditional and historical knowledge
- In-vitro evidence
- In-vivo/preclinical evidence
- Human evidence
- Systematic reviews and meta-analyses
- Evidence limitations
- Contradictory evidence
- Source provenance
- Claim traceability
- Evidence-strength classification
- Translation gaps
- Reproducibility

Only publicly available and academically or regulatorily credible sources are used.

---

## 3. Non-Goals

This project does not include:

- Laboratory experimentation
- Animal experimentation
- Clinical experimentation
- Patient-facing medical advice
- Manufacturing process development
- Controlled or restricted substances
- Cannabis-related work
- Product approval
- Regulatory approval claims
- Commercial strategy
- Unsupported efficacy or safety claims

---

## 4. Core Evidence Workflow

The framework follows this workflow:

Public source

↓

Source registration

↓

Evidence classification

↓

Claim extraction

↓

Claim-to-evidence linkage

↓

Evidence-strength assessment

↓

Limitation recording

↓

Contradiction detection

↓

Translation-gap identification

↓

Future R&D decision input

---

## 5. Evidence Hierarchy

Evidence is classified according to the type and inferential role of the evidence.

The framework distinguishes:

1. Systematic reviews and meta-analyses
2. Randomized controlled human studies
3. Other human studies
4. Animal/in-vivo studies
5. In-vitro studies
6. Traditional or historical knowledge
7. Expert or narrative information

Evidence level alone does not establish truth or clinical effectiveness.

---

## 6. Traditional Knowledge Boundary

Traditional or historical use is recorded as historical evidence.

It may help generate a research hypothesis, but it is not treated as automatic evidence of:

- Clinical efficacy
- Clinical safety
- Appropriate dose
- Product suitability
- Manufacturing suitability
- Regulatory approval

The framework therefore keeps:

Traditional knowledge

→

Research hypothesis

separate from:

Scientific evidence

→

Clinical interpretation

---

## 7. Evidence Strength

Evidence-strength classifications used in this project are:

- HIGH
- MODERATE
- LOW
- VERY LOW
- INSUFFICIENT
- UNKNOWN

These classifications are used as structured evidence-quality labels and are not presented as a formal GRADE assessment unless a complete formal GRADE process has been performed.

---

## 8. Source Provenance

Every source receives a unique `source_id`.

Every evidence record receives a unique `evidence_id`.

Every claim receives a unique `claim_id`.

Every contradiction receives a unique `contradiction_id`.

The framework preserves:

- Source identity
- Publication information
- Source type
- Source identifier or URL
- Access date
- Version information
- Provenance notes

---

## 9. Claim Traceability

Every proposed scientific statement must be traceable through:

`claim_id`

↓

`evidence_id`

↓

`source_id`

↓

Original public source

Claims without sufficient source support are not treated as established findings.

---

## 10. Contradiction Handling

Contradictory findings are not silently resolved.

Where sources differ, the framework records:

- Source A
- Source B
- Conflict type
- Different findings
- Possible explanation
- Resolution status
- Final interpretation

Possible explanations include:

- Different populations
- Different formulations
- Different doses
- Different study designs
- Different outcomes
- Different study durations
- Risk of bias
- Heterogeneity
- Different evidence-certainty approaches

If the contradiction cannot be responsibly resolved, it remains open.

---

## 11. Translation Gap

The framework separates:

### Known

Information directly supported by available evidence.

### Uncertain

Questions where evidence exists but certainty or generalizability is limited.

### Further R&D

Questions that require additional scientific investigation.

### Formulation Work

Questions requiring separate formulation-development investigation.

### Safety Validation

Questions requiring appropriate safety assessment.

### Regulatory Assessment

Questions requiring assessment under the applicable jurisdiction and product category.

Unknown information is retained as `UNKNOWN` rather than inferred.

---

## 12. Reproducibility

Another researcher should be able to:

1. Select a non-sensitive botanical or biological concept.
2. Define the research question.
3. Apply source inclusion and exclusion criteria.
4. Search public scientific sources.
5. Register each source.
6. Extract evidence.
7. Assign evidence identifiers.
8. Link claims to evidence and sources.
9. Record limitations.
10. Identify contradictions.
11. Preserve unresolved contradictions.
12. Identify translation gaps.
13. Record unknowns explicitly.
14. Conduct quality-control review.

The framework is intended to be reusable rather than limited to one botanical concept.

---

## 13. Repository Structure

```text
BHIV_Test_Task_2/
│
├── README.md
│
├── evidence_framework/
│   ├── methodology.md
│   ├── evidence_schema.json
│   ├── source_register.csv
│   ├── evidence_map.csv
│   ├── claim_traceability.csv
│   ├── contradiction_register.csv
│   └── translation_gap_register.md
│
├── sample_implementation/
│   └── sample_evidence_record.json
│
├── DEP/
│   ├── metadata.md
│   ├── tms.md
│   ├── gc.md
│   ├── mdu.md
│   ├── review.md
│   ├── next_tasks.md
│   ├── blockers.md
│   └── screenshots/
│
└── evidence_packet/
    ├── review_packet.md
    ├── screenshots/
    ├── code_packet/
    ├── runtime_logs/
    ├── api_samples/
    └── deployment_proof/