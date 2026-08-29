# Candidate Evidence Dataset

## Biosimilarity & Preclinical Evidence Quality Foundation

**Project:** Biosimilarity & Preclinical Evidence Quality Foundation  
**Document:** Candidate Evidence Dataset  
**Version:** v1.0  
**Status:** Working  
**Dataset Type:** SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING  
**Last Updated:** 2026-08-21

---

# 1. Purpose

This document describes the sample evidence dataset used by the
Biosimilarity Evidence Tracker.

The dataset is designed to demonstrate how biosimilarity and
preclinical evidence can be represented as structured records.

The records are intentionally fictional.

They are created only for:

- Software testing
- Python-program development
- Evidence organization practice
- QC model testing
- Search and filtering demonstrations
- Comparison demonstrations
- JSON-output testing

---

# 2. Critical Scientific Disclaimer

> **ALL RECORDS IN THIS DOCUMENT ARE SAMPLE / SYNTHETIC / FOR SOFTWARE
> TESTING.**

The records below are **not published experimental results**.

They do not represent:

- Actual laboratory experiments
- Actual animal experiments
- Actual clinical studies
- Actual pharmaceutical products
- Actual regulatory submissions
- Actual FDA findings
- Actual EMA findings
- Actual WHO findings
- Actual biosimilar approval evidence

No synthetic result in this dataset should be interpreted as evidence
that a candidate product is biosimilar.

---

# 3. Dataset Objective

The dataset provides structured examples for the following workflow:

```text
Synthetic Evidence Record
        ↓
CSV Dataset
        ↓
Python Evidence Tracker
        ↓
Search
        ↓
Filter
        ↓
QC Review
        ↓
Evidence Comparison
        ↓
Limitation Detection
        ↓
JSON Output
Dataset Fields
The dataset uses the following fields.
Field	Description
Evidence ID	Unique identifier for the evidence record
Reference Product	Fictional reference product
Candidate Product	Fictional candidate product
Evidence Category	Type of evidence
Study/Source	Source or study description
Measurement	Measurement or evidence type
Result	Sample result description
Control	Comparison/control information
Evidence Quality	QC classification
Validation Status	Validation status of the method/evidence
Limitation	Known limitation of the record
Reviewer Note	Human-review note


5. Evidence Categories Used
The sample dataset uses the following evidence categories:
1. Analytical
2. Structural
3. Functional
4. Pharmacokinetic
5. Pharmacodynamic
6. Immunogenicity
7. Preclinical
8. Clinical
These categories are used only to demonstrate evidence organization.
6. Evidence Quality Statuses
The dataset uses the QC statuses defined in
EVIDENCE_QC_MODEL.md.
VERIFIED
The record contains sufficient information for the intended
organizational purpose.
PARTIAL
Some information is available, but important information is incomplete.
NEEDS REVIEW
Additional human review is required.
CONFLICTING
The available evidence contains an unresolved inconsistency.
INSUFFICIENT
The available information is not sufficient for the intended
organizational purpose.
7. Validation Statuses
The dataset uses the following validation statuses:
VERIFIED
PARTIAL
NEEDS REVIEW
INSUFFICIENT
These statuses refer to the documented validation/review condition of
the evidence record.
They do not mean that the candidate product has been scientifically or
regulatorily approved.
8. Synthetic Evidence Records
Record 1
Evidence ID
EV-001
Reference Product
Reference-A
Candidate Product
Candidate-B
Evidence Category
Analytical
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Analytical comparison example
Measurement
Example chromatographic similarity measurement
Result
Synthetic result indicating high similarity for software testing
Control
Reference-A
Evidence Quality
VERIFIED
Validation Status
VERIFIED
Limitation
Synthetic record; no real experimental data are represented.
Reviewer Note
Record is complete for software testing. Human scientific review would be required for real evidence.
Record 2
Evidence ID
EV-002
Reference Product
Reference-A
Candidate Product
Candidate-B
Evidence Category
Structural
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Structural characterization example
Measurement
Example mass-spectrometry-based structural characterization
Result
Synthetic result indicating comparable structural characteristics
Control
Reference-A
Evidence Quality
VERIFIED
Validation Status
VERIFIED
Limitation
Synthetic record; structural similarity alone does not establish clinical equivalence.
Reviewer Note
Used to test structural evidence filtering.
Record 3
Evidence ID
EV-003
Reference Product
Reference-A
Candidate Product
Candidate-B
Evidence Category
Functional
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Functional comparison example
Measurement
Example biological activity assay
Result
Synthetic result indicating comparable functional activity
Control
Reference-A
Evidence Quality
VERIFIED
Validation Status
VERIFIED
Limitation
Synthetic functional result; does not independently establish patient safety or efficacy.
Reviewer Note
Record is intended for functional evidence demonstration.
Record 4
Evidence ID
EV-004
Reference Product
Reference-A
Candidate Product
Candidate-B
Evidence Category
Pharmacokinetic
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - PK evidence example
Measurement
Example pharmacokinetic exposure measurement
Result
Synthetic result indicating comparable exposure pattern
Control
Reference-A
Evidence Quality
PARTIAL
Validation Status
PARTIAL
Limitation
Synthetic record with incomplete supporting statistical information.
Reviewer Note
Additional review would be required before interpreting the evidence.
Record 5
Evidence ID
EV-005
Reference Product
Reference-A
Candidate Product
Candidate-B
Evidence Category
Pharmacodynamic
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - PD evidence example
Measurement
Example pharmacodynamic biomarker measurement
Result
Synthetic result showing a comparable example biomarker response
Control
Reference-A
Evidence Quality
NEEDS REVIEW
Validation Status
NEEDS REVIEW
Limitation
Method validation information is intentionally incomplete in this synthetic record.
Reviewer Note
Used to test the NEEDS REVIEW status.
Record 6
Evidence ID
EV-006
Reference Product
Reference-A
Candidate Product
Candidate-B
Evidence Category
Immunogenicity
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Immunogenicity example
Measurement
Example anti-drug antibody assessment
Result
Synthetic result indicating no major difference in the example dataset
Control
Reference-A
Evidence Quality
INSUFFICIENT
Validation Status
INSUFFICIENT
Limitation
Synthetic record lacks sufficient supporting information for interpretation.
Reviewer Note
Evidence gap intentionally included to test incomplete-evidence detection.
Record 7
Evidence ID
EV-007
Reference Product
Reference-A
Candidate Product
Candidate-B
Evidence Category
Preclinical
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Preclinical evidence example
Measurement
Example comparative preclinical observation
Result
Synthetic record containing a hypothetical comparable observation
Control
Reference-A
Evidence Quality
PARTIAL
Validation Status
PARTIAL
Limitation
Study documentation and complete supporting data are not included.
Reviewer Note
Used to test incomplete preclinical evidence.
Record 8
Evidence ID
EV-008
Reference Product
Reference-A
Candidate Product
Candidate-B
Evidence Category
Clinical
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Clinical evidence example
Measurement
Example clinical outcome comparison
Result
Synthetic result for software testing only
Control
Reference-A
Evidence Quality
NEEDS REVIEW
Validation Status
NEEDS REVIEW
Limitation
No real clinical data are represented; this record is entirely synthetic.
Reviewer Note
Included to demonstrate the clinical evidence category in the tracker.
Record 9
Evidence ID
EV-009
Reference Product
Reference-A
Candidate Product
Candidate-C
Evidence Category
Analytical
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Second candidate analytical example
Measurement
Example analytical characterization
Result
Synthetic result containing an unresolved difference for testing
Control
Reference-A
Evidence Quality
CONFLICTING
Validation Status
NEEDS REVIEW
Limitation
Synthetic records contain an unresolved evidence difference.
Reviewer Note
Used to test conflicting-evidence handling.
Record 10
Evidence ID
EV-010
Reference Product
Reference-A
Candidate Product
Candidate-C
Evidence Category
Preclinical
Study/Source
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Second candidate preclinical example
Measurement
Example preclinical measurement
Result
Synthetic record with incomplete study information
Control
Reference-A
Evidence Quality
INSUFFICIENT
Validation Status
INSUFFICIENT
Limitation
Study details and supporting information are incomplete.
Reviewer Note
Used to test incomplete evidence detection and comparison with missing categories.
9. Summary of Synthetic Dataset
Evidence ID	Candidate	Category	Evidence Quality	Validation Status
EV-001	Candidate-B	Analytical	VERIFIED	VERIFIED
EV-002	Candidate-B	Structural	VERIFIED	VERIFIED
EV-003	Candidate-B	Functional	VERIFIED	VERIFIED
EV-004	Candidate-B	Pharmacokinetic	PARTIAL	PARTIAL
EV-005	Candidate-B	Pharmacodynamic	NEEDS REVIEW	NEEDS REVIEW
EV-006	Candidate-B	Immunogenicity	INSUFFICIENT	INSUFFICIENT
EV-007	Candidate-B	Preclinical	PARTIAL	PARTIAL
EV-008	Candidate-B	Clinical	NEEDS REVIEW	NEEDS REVIEW
EV-009	Candidate-C	Analytical	CONFLICTING	NEEDS REVIEW
EV-010	Candidate-C	Preclinical	INSUFFICIENT	INSUFFICIENT


10. Candidate-B Evidence Summary
The synthetic dataset contains the following records for Candidate-B:
Evidence Records: 8

Analytical: 1
Structural: 1
Functional: 1
Pharmacokinetic: 1
Pharmacodynamic: 1
Immunogenicity: 1
Preclinical: 1
Clinical: 1
Synthetic Quality Distribution
VERIFIED: 3
PARTIAL: 2
NEEDS REVIEW: 2
INSUFFICIENT: 1
CONFLICTING: 0
Synthetic Evidence Gap
Immunogenicity evidence is intentionally marked INSUFFICIENT.
This is a software-testing condition, not a scientific conclusion
about any real product.
11. Candidate-C Evidence Summary
The synthetic dataset contains the following records for Candidate-C:
Evidence Records: 2

Analytical: 1
Preclinical: 1
Synthetic Quality Distribution
VERIFIED: 0
PARTIAL: 0
NEEDS REVIEW: 0
INSUFFICIENT: 1
CONFLICTING: 1
Synthetic Evidence Gaps
Structural evidence: not represented
Functional evidence: not represented
PK evidence: not represented
PD evidence: not represented
Immunogenicity evidence: not represented
Clinical evidence: not represented
These are dataset-level gaps only.
They do not represent real-world evidence gaps.
12. Why Synthetic Records Are Used
Synthetic records allow the Python Evidence Tracker to be tested without
using or fabricating real experimental results.
The records demonstrate:
- Search functionality
- Filtering
- Validation-status filtering
- Evidence-quality filtering
- Missing-evidence detection
- Conflict detection
- Candidate comparison
- JSON generation
- Error handling
13. CSV Dataset
The Python program uses a CSV file located at:
sample_data/candidate_evidence.csv
The first row contains the field names:
Evidence ID,Reference Product,Candidate Product,Evidence Category,Study/Source,Measurement,Result,Control,Evidence Quality,Validation Status,Limitation,Reviewer Note
The CSV contains the same 10 synthetic records described in this
document.
14. Ready-to-Paste CSV Data
The following data can be used in:
sample_data/candidate_evidence.csv
Evidence ID,Reference Product,Candidate Product,Evidence Category,Study/Source,Measurement,Result,Control,Evidence Quality,Validation Status,Limitation,Reviewer Note
EV-001,Reference-A,Candidate-B,Analytical,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Analytical comparison example,Example chromatographic similarity measurement,Synthetic result indicating high similarity for software testing,Reference-A,VERIFIED,VERIFIED,Synthetic record; no real experimental data are represented.,Record is complete for software testing. Human scientific review would be required for real evidence.
EV-002,Reference-A,Candidate-B,Structural,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Structural characterization example,Example mass-spectrometry-based structural characterization,Synthetic result indicating comparable structural characteristics,Reference-A,VERIFIED,VERIFIED,Synthetic record; structural similarity alone does not establish clinical equivalence.,Used to test structural evidence filtering.
EV-003,Reference-A,Candidate-B,Functional,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Functional comparison example,Example biological activity assay,Synthetic result indicating comparable functional activity,Reference-A,VERIFIED,VERIFIED,Synthetic functional result; does not independently establish patient safety or efficacy.,Record is intended for functional evidence demonstration.
EV-004,Reference-A,Candidate-B,Pharmacokinetic,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - PK evidence example,Example pharmacokinetic exposure measurement,Synthetic result indicating comparable exposure pattern,Reference-A,PARTIAL,PARTIAL,Synthetic record with incomplete supporting statistical information.,Additional review would be required before interpreting the evidence.
EV-005,Reference-A,Candidate-B,Pharmacodynamic,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - PD evidence example,Example pharmacodynamic biomarker measurement,Synthetic result showing a comparable example biomarker response,Reference-A,NEEDS REVIEW,NEEDS REVIEW,Method validation information is intentionally incomplete in this synthetic record.,Used to test the NEEDS REVIEW status.
EV-006,Reference-A,Candidate-B,Immunogenicity,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Immunogenicity example,Example anti-drug antibody assessment,Synthetic result indicating no major difference in the example dataset,Reference-A,INSUFFICIENT,INSUFFICIENT,Synthetic record lacks sufficient supporting information for interpretation.,Evidence gap intentionally included to test incomplete-evidence detection.
EV-007,Reference-A,Candidate-B,Preclinical,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Preclinical evidence example,Example comparative preclinical observation,Synthetic record containing a hypothetical comparable observation,Reference-A,PARTIAL,PARTIAL,Study documentation and complete supporting data are not included.,Used to test incomplete preclinical evidence.
EV-008,Reference-A,Candidate-B,Clinical,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Clinical evidence example,Example clinical outcome comparison,Synthetic result for software testing only,Reference-A,NEEDS REVIEW,NEEDS REVIEW,No real clinical data are represented; this record is entirely synthetic.,Included to demonstrate the clinical evidence category in the tracker.
EV-009,Reference-A,Candidate-C,Analytical,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Second candidate analytical example,Example analytical characterization,Synthetic result containing an unresolved difference for testing,Reference-A,CONFLICTING,NEEDS REVIEW,Synthetic records contain an unresolved evidence difference.,Used to test conflicting-evidence handling.
EV-010,Reference-A,Candidate-C,Preclinical,SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING - Second candidate preclinical example,Example preclinical measurement,Synthetic record with incomplete study information,Reference-A,INSUFFICIENT,INSUFFICIENT,Study details and supporting information are incomplete.,Used to test incomplete evidence detection and comparison with missing categories.
15. Dataset Validation Rules
The Python Evidence Tracker should check the following rules.
Rule 1 — Evidence ID
Every record must have an Evidence ID.
Example:
EV-001
A missing Evidence ID should be treated as an invalid or incomplete
record.
Rule 2 — Evidence ID Uniqueness
Every Evidence ID should be unique.
Example of valid IDs:
EV-001
EV-002
EV-003
Duplicate IDs should be flagged during testing.
Rule 3 — Candidate Product
Every record should contain a Candidate Product.
Example:
Candidate-B
A missing candidate should be flagged as incomplete.
Rule 4 — Evidence Category
Every record should contain an Evidence Category.
Valid sample categories include:
Analytical
Structural
Functional
Pharmacokinetic
Pharmacodynamic
Immunogenicity
Preclinical
Clinical
Rule 5 — Evidence Quality
Evidence Quality should use an accepted status:
VERIFIED
PARTIAL
NEEDS REVIEW
CONFLICTING
INSUFFICIENT
An unknown value should be flagged.
Rule 6 — Validation Status
Validation Status should use an accepted value:
VERIFIED
PARTIAL
NEEDS REVIEW
INSUFFICIENT
An invalid value should be flagged.
Rule 7 — Limitation
Every record should contain a limitation.
This ensures that the tracker does not hide uncertainty.
Rule 8 — Synthetic Label
Every sample record should clearly indicate:
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING
16. Dataset Quality-Control Checklist
Before using the CSV with Python, verify:
- File name is candidate_evidence.csv.
- File is inside sample_data/.
- Header row is present.
- All 10 records are present.
- Evidence IDs are unique.
- Candidate products are present.
- Reference products are present.
- Evidence categories are present.
- Evidence quality values are valid.
- Validation status values are valid.
- Limitations are present.
- Reviewer notes are present.
- Synthetic label is present.
- No record is presented as real experimental evidence.
17. Dataset-to-Python Mapping
The Python program can use the following mapping:
CSV Column
    ↓
Evidence Record
    ↓
Search / Filter
    ↓
QC Status
    ↓
Limitation Detection
    ↓
Candidate Comparison
    ↓
JSON Output
For example:
Candidate Product
        ↓
Candidate-B
        ↓
8 evidence records
        ↓
Filter by category
        ↓
Analytical / Functional / Preclinical
        ↓
Display quality and limitations
18. Example Software Output
A possible output for the synthetic dataset is:
Biosimilarity Evidence Review

Candidate:
Candidate-B

Evidence Categories:
Analytical
Structural
Functional
Pharmacokinetic
Pharmacodynamic
Immunogenicity
Preclinical
Clinical

Evidence Records:
8

Verified:
3

Needs Review:
2

Insufficient:
1

Known Evidence Gaps:
Immunogenicity evidence is incomplete in the synthetic test dataset.
This output is only a software demonstration.
It is not a scientific or regulatory conclusion.
19. Example JSON Output
The Python tracker may produce structured output such as:
{
  "candidate": "Candidate-B",
  "reference": "Reference-A",
  "evidence_records": 8,
  "categories": [
    "Analytical",
    "Structural",
    "Functional",
    "Pharmacokinetic",
    "Pharmacodynamic",
    "Immunogenicity",
    "Preclinical",
    "Clinical"
  ],
  "quality_summary": {
    "VERIFIED": 3,
    "PARTIAL": 2,
    "NEEDS REVIEW": 2,
    "INSUFFICIENT": 1,
    "CONFLICTING": 0
  },
  "known_evidence_gaps": [
    "Immunogenicity evidence is incomplete in the synthetic test dataset"
  ],
  "data_type": "SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING"
}
20. Important Interpretation Rule
The following output:
Verified: 3
does not mean:
The candidate is biosimilar.
The following output:
Insufficient: 1
does not mean:
The candidate failed.
The software only organizes the evidence records and their documented
QC status.
21. Relationship to Evidence QC Model
This dataset follows the rules described in:
EVIDENCE_QC_MODEL.md
The relationship is:
EVIDENCE_QC_MODEL.md
        ↓
Defines QC fields and statuses
        ↓
CANDIDATE_EVIDENCE_DATASET.md
        ↓
Explains synthetic records
        ↓
candidate_evidence.csv
        ↓
Python Evidence Tracker
22. Dataset Limitations
This dataset has several limitations.
Synthetic Data
All records are fictional.
No Real Experimental Results
No measurements represent actual laboratory results.
No Regulatory Evidence
The dataset cannot support a regulatory submission or approval
decision.
Simplified Structure
Real scientific evidence can contain significantly more information.
No Raw Data
The dataset does not contain actual raw analytical, preclinical, or
clinical data.
No Statistical Dataset
The numerical/statistical content required for real scientific
evaluation is intentionally absent.
No Clinical Interpretation
The dataset does not establish clinical safety or efficacy.
23. Future Dataset Improvements
Future versions may include additional structured fields such as:
Study Date
Study Type
Species
Study Population
Sample Batch
Protocol Version
Method Version
Instrument ID
Raw Data Location
Statistical Method
Missing Data Description
Protocol Deviation
Reviewer ID
Review Date
Evidence Source URL
Source Publication Date
Evidence Confidence
Any additional fields should be introduced carefully and should not
create unsupported scientific conclusions.
24. Responsible Data Handling
The project follows these principles:
1. Never fabricate published data.
2. Clearly label synthetic records.
3. Preserve source traceability.
4. Record limitations.
5. Do not hide missing information.
6. Do not automatically resolve conflicting evidence.
7. Keep scientific interpretation separate from software output.
8. Use human review for important scientific decisions.
25. Final Dataset Statement
The Candidate Evidence Dataset provides a controlled synthetic dataset
for testing the Biosimilarity Evidence Tracker.
Its main purpose is to demonstrate how evidence can be:
Recorded
   ↓
Classified
   ↓
Quality-checked
   ↓
Filtered
   ↓
Compared
   ↓
Reviewed
   ↓
Exported as structured data
The dataset is intentionally fictional and must not be represented as
real scientific evidence.