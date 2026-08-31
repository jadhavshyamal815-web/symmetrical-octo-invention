# Evidence Methodology

## 1. Purpose

This methodology defines how publicly available scientific evidence is collected, classified, evaluated and mapped for the selected concept:

**Curcuma longa L. (turmeric/curcumin) — evidence mapping related to knee osteoarthritis.**

The purpose is to create a reusable evidence-to-translation workflow.

This methodology does not attempt to prove therapeutic efficacy, safety, manufacturing suitability, regulatory approval or commercial viability.

---

## 2. Research Scope

The evidence workflow covers:

- Traditional and historical knowledge
- Research hypotheses
- In-vitro evidence
- In-vivo/preclinical evidence
- Human evidence
- Systematic reviews
- Meta-analyses
- Contradictory evidence
- Evidence limitations
- Source provenance
- Claim traceability
- Translation gaps
- Reproducibility

Only publicly available sources are considered.

---

## 3. Evidence Hierarchy

Evidence is classified according to study type and its position in the scientific evidence pathway.

### Level 1 — Systematic Reviews and Meta-Analyses

These synthesize findings from multiple studies.

They may provide a broader view of the available evidence, but their reliability depends on the quality, consistency and applicability of the included studies.

### Level 2 — Randomized Controlled Human Studies

Randomized controlled studies can provide direct evidence about outcomes in human participants.

Their interpretation depends on study quality, sample size, duration, outcome selection, comparator and other methodological factors.

### Level 3 — Other Human Studies

This includes observational and other non-randomized human research.

Such evidence may provide useful information but can have limitations related to confounding, selection bias and causal interpretation.

### Level 4 — In-Vivo / Animal Evidence

Animal studies provide preclinical evidence and may help investigate biological effects or mechanisms.

Animal findings cannot automatically be extrapolated to humans.

### Level 5 — In-Vitro Evidence

In-vitro studies investigate biological activity under controlled laboratory conditions.

They can contribute to mechanistic understanding but do not independently establish clinical effectiveness.

### Level 6 — Traditional or Historical Knowledge

Traditional knowledge records historical use or cultural context.

It may contribute to hypothesis generation but is not treated as proof of efficacy or safety.

### Level 7 — Expert or Narrative Information

Expert commentary and narrative material may provide context but should not replace primary scientific evidence.

---

## 4. Traditional Knowledge Boundary

Traditional or historical information must remain separate from modern scientific evidence.

The framework uses the following interpretation pathway:

Traditional knowledge

↓

Research hypothesis

↓

Scientific investigation

Traditional use does not automatically establish:

- Clinical efficacy
- Clinical safety
- Appropriate dose
- Product suitability
- Manufacturing suitability
- Regulatory approval

Historical mention is therefore recorded as historical evidence rather than scientific validation.

---

## 5. Scientific Evidence Classification

Each evidence record is assigned an evidence category.

The main categories are:

- TRADITIONAL_KNOWLEDGE
- IN_VITRO
- IN_VIVO
- HUMAN_OBSERVATIONAL
- HUMAN_RANDOMIZED
- SYSTEMATIC_REVIEW
- META_ANALYSIS
- OTHER

The category describes the evidence type and does not by itself determine evidence certainty.

---

## 6. Source Selection Criteria

Sources should be selected using the following criteria:

### Include

- Peer-reviewed scientific publications
- PubMed-indexed publications
- Systematic reviews
- Meta-analyses
- Randomized controlled trials
- Relevant observational studies
- Public government health information
- WHO publications where relevant
- NIH/NCCIH publications where relevant
- Cochrane evidence resources
- Other academically or regulatorily credible public sources

### Source Quality Considerations

Each source should be assessed for:

- Authority
- Relevance
- Publication provenance
- Study design
- Recency
- Methodological transparency
- Availability of identifiable publication information

---

## 7. Exclusion Criteria

The following should not be used as primary scientific evidence:

- Marketing webpages
- Commercial product advertisements
- Supplement-company promotional claims
- Unsourced blogs
- Social-media claims
- AI-generated citations
- Anonymous claims
- Sources without identifiable provenance
- Duplicate records
- Sources outside the defined research question

A source may be retained for background context only when its role is explicitly identified and it is not presented as scientific proof.

---

## 8. Evidence Extraction

For each source, the following information should be extracted where available:

1. Source identifier
2. Evidence identifier
3. Concept
4. Evidence category
5. Study design
6. Population or experimental model
7. Intervention or exposure
8. Comparator
9. Outcome
10. Main finding
11. Evidence strength
12. Limitations
13. Contradiction status
14. Provenance information

If information cannot be verified from the source, it must be recorded as:

`UNKNOWN`

The researcher must not infer missing information.

---

## 9. Evidence Strength Model

The framework uses the following evidence-strength categories:

- HIGH
- MODERATE
- LOW
- VERY LOW
- INSUFFICIENT
- UNKNOWN

These categories are used as structured evidence-quality labels.

They are informed by established evidence-quality concepts, including considerations commonly used in GRADE-type approaches.

This framework does not claim to perform a formal GRADE assessment unless the complete formal GRADE methodology has been applied.

---

## 10. Factors Affecting Evidence Strength

Evidence strength should consider, where applicable:

### Risk of Bias

Whether study design or execution may introduce systematic error.

### Inconsistency

Whether different studies report substantially different findings.

### Indirectness

Whether the evidence directly addresses the research question, population, intervention and outcome of interest.

### Imprecision

Whether sample size, confidence intervals or other factors create substantial uncertainty.

### Publication Bias

Whether the available literature may not represent all conducted studies.

### Study Design

The design and methodological quality of the study should be considered when interpreting evidence.

---

## 11. Claim Traceability

Every scientific claim must have a unique `claim_id`.

Each claim should link to:

`claim_id`

↓

`evidence_id`

↓

`source_id`

↓

Original source

The claim record must also include:

- Evidence type
- Evidence strength
- Limitations
- Contradiction status
- Provenance note
- Translation status

Claims without sufficient source support should not be presented as established findings.

---

## 12. Contradiction Handling

Contradictory evidence must remain visible.

The framework does not silently select the preferred study or interpretation.

When two sources differ, the contradiction register should record:

- Contradiction identifier
- Related claim
- Source A
- Source B
- Conflict type
- Source A position
- Source B position
- Possible explanation
- Resolution status
- Final interpretation

Possible explanations for differences include:

- Different study populations
- Different formulations
- Different doses
- Different study designs
- Different outcome measures
- Different study durations
- Risk of bias
- Statistical heterogeneity
- Different inclusion criteria
- Different evidence-certainty approaches

If a contradiction cannot be responsibly resolved, its status remains:

`OPEN`

---

## 13. Unsupported Claims

Absolute claims require particularly strong evidence.

Examples of unsupported claim patterns include:

- "Proven to cure"
- "Guaranteed to work"
- "Completely safe"
- "Scientifically proven for everyone"
- "Approved"
- "No side effects"

The framework should downgrade or reject claims when available evidence does not justify the wording.

An unsupported claim should be classified as:

`INSUFFICIENT`

or

`UNKNOWN`

or

`UNSUPPORTED`

as appropriate.

---

## 14. Translation Gap Analysis

The framework separates evidence from product-development decisions.

Translation analysis should identify:

### Known

What is directly supported by available evidence.

### Uncertain

What has evidence but remains uncertain because of limitations, inconsistency or indirectness.

### Further R&D

Questions that require additional scientific research.

### Formulation Work

Questions that would require separate formulation-development work.

### Safety Validation

Questions that require appropriate safety assessment.

### Regulatory Assessment

Questions requiring assessment under the applicable regulatory framework and intended product category.

No formulation, manufacturing process or regulatory outcome is assumed.

---

## 15. Provenance Rules

Every source must have a unique `source_id`.

Every evidence record must have a unique `evidence_id`.

Every claim must have a unique `claim_id`.

Every contradiction must have a unique `contradiction_id`.

Source records should preserve:

- Title
- Authors or organization
- Publication year
- Source type
- Journal or organization
- Identifier or URL
- Access date
- Version
- Provenance note

The original source should remain identifiable from every downstream evidence record.

---

## 16. Versioning

Evidence records should contain version information.

Example:

`1.0` — Initial evidence extraction

`1.1` — Minor correction to metadata

`2.0` — Major revision following new evidence or substantial interpretation change

Important changes must not be silently overwritten.

---

## 17. Reproducibility

Another researcher should be able to repeat the workflow by following these steps:

1. Select a non-sensitive botanical or biological concept.
2. Define the research question.
3. Apply source inclusion criteria.
4. Apply source exclusion criteria.
5. Search appropriate public scientific sources.
6. Register each source.
7. Extract evidence.
8. Assign evidence identifiers.
9. Classify evidence type.
10. Record limitations.
11. Create traceable claims.
12. Link claims to evidence and sources.
13. Identify contradictions.
14. Preserve unresolved contradictions.
15. Identify translation gaps.
16. Record unknown information explicitly.
17. Conduct quality-control review.
18. Package the results for independent review.

---

## 18. Limitations of the Methodology

This framework is an evidence-mapping system and is not itself a formal systematic review.

Potential limitations include:

- Incomplete literature retrieval
- Restricted access to some full-text publications
- Differences in study design
- Differences in botanical preparations
- Differences in populations
- Differences in intervention characteristics
- Statistical heterogeneity
- Risk of bias
- Publication bias
- Researcher judgment during evidence classification

These limitations should be recorded rather than hidden.

---

## 19. Known Unknowns

The following information remains unknown unless independently verified:

- Final Test Task 1 evaluation status
- Exact source-pack availability
- Product-specific efficacy
- Product-specific safety
- Manufacturing suitability
- Commercial viability
- Regulatory outcome for a hypothetical product

Unknown information must remain explicitly marked as `UNKNOWN`.

---

## 20. Scientific Interpretation Rule

The framework follows this principle:

Traditional knowledge

does not equal

scientific validation.

Preclinical evidence

does not equal

clinical effectiveness.

Human evidence

does not automatically equal

universal effectiveness.

Scientific evidence

does not automatically equal

product approval.

The purpose of the framework is to preserve these distinctions.

---

## 21. Quality-Control Principle

Before an evidence record is considered review-ready, the following questions must be answered:

- Is the source identifiable?
- Is the evidence type correctly classified?
- Is the claim supported by the source?
- Are limitations recorded?
- Is evidence strength justified?
- Are contradictions visible?
- Are unknowns preserved?
- Is provenance retained?
- Can another researcher reproduce the interpretation?

If any answer is no, the record requires further review.

---

## 22. Final Methodology Principle

The objective is not to create a persuasive document.

The objective is to create a traceable evidence system that allows another researcher to determine:

**What is known?**

**What is supported?**

**How strong is the evidence?**

**What contradicts it?**

**What remains uncertain?**

**What would require further research?**

**What should not yet be claimed?**