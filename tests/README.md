# Biosimilarity & Preclinical Evidence Tracker

## 1. Project Overview

This project is a Biosimilarity & Preclinical Evidence Quality Foundation
mini-build developed as part of the Biotech Learnship – Test 1.

The project focuses on organizing, documenting, comparing, and quality-
checking biosimilarity and preclinical evidence.

A simple Python-based Evidence Tracker is included to organize sample
evidence records stored in a CSV file.

The workflow followed in this project is:

Research Study
→ Experimental Evidence
→ Quality Control
→ Evidence Documentation
→ Comparison
→ Interpretation
→ Human Review
→ Research Decision

The project is designed as an evidence-organization and learning
framework. It is not intended to make regulatory or clinical decisions.

---

## 2. Objective

The main objective of this project is to build a structured Biosimilarity
& Preclinical Evidence Map and a simple evidence tracker.

The project aims to:

- Understand the fundamentals of biosimilars.
- Understand major categories of biosimilarity evidence.
- Understand preclinical and animal-study evidence at a conceptual level.
- Organize evidence into structured records.
- Apply basic evidence quality-control principles.
- Identify incomplete or conflicting evidence.
- Compare reference-product and candidate-product evidence records.
- Generate structured JSON output.
- Document assumptions, limitations, and evidence gaps.

---

## 3. Scope

This project covers:

- Biologics and biosimilars
- Reference biological products
- Biosimilar development concepts
- Analytical evidence
- Structural evidence
- Functional evidence
- Pharmacokinetic (PK) evidence
- Pharmacodynamic (PD) evidence
- Immunogenicity
- Preclinical evidence
- Clinical evidence
- Evidence quality control
- Data integrity
- Reproducibility
- Evidence comparison
- Basic Python programming
- CSV-based evidence organization

The project does not include laboratory experiments, animal experiments,
clinical decision-making, or regulatory approval activities.

---

## 4. Repository Structure

The project is organized as follows:

```text
BIOSIMILARITY PROJECT/
│
├── README.md
├── BIOSIMILARITY_RESEARCH.md
├── PRECLINICAL_EVIDENCE_MAP.md
├── SOURCE_REGISTRY.md
├── EVIDENCE_QC_MODEL.md
├── CANDIDATE_EVIDENCE_DATASET.md
├── LEARNING_NOTES.md
├── REVIEW_PACKET.md
│
├── evidence_tracker.py
│
├── sample_data/
│   └── candidate_evidence.csv
│
├── tests/
│   └── TEST_RESULTS.md
│
└── screenshots/
| File/Folder | Purpose |
|---|---|
| `README.md` | Project overview and instructions |
| `BIOSIMILARITY_RESEARCH.md` | Biosimilarity research and glossary |
| `PRECLINICAL_EVIDENCE_MAP.md` | Evidence categories and preclinical evidence map |
| `SOURCE_REGISTRY.md` | Authoritative research sources |
| `EVIDENCE_QC_MODEL.md` | Evidence quality-control framework |
| `CANDIDATE_EVIDENCE_DATASET.md` | Documentation of the sample dataset |
| `LEARNING_NOTES.md` | Learning and problem-solving notes |
| `REVIEW_PACKET.md` | Final review and handover information |
| `evidence_tracker.py` | Python evidence tracker |
| `sample_data/` | CSV evidence dataset |
| `tests/` | Testing documentation |
| `screenshots/` | Screenshots demonstrating project execution |
Requirements
The mini-build requires:
- Python 3.x
- Visual Studio Code or another Python-compatible editor
- The project files included in this repository
- The sample CSV dataset
The Python tracker uses standard Python libraries.
No laboratory equipment, animal experiments, or clinical data are
required for this mini-build.
How to Run the Python Program
Step 1 — Open the project
Open the BIOSIMILARITY PROJECT folder in Visual Studio Code.
Step 2 — Open the terminal
In VS Code, select:
Terminal → New Terminal
The terminal should be opened in the project folder.
For example:
PS C:\Users\<YourName>\...\BIOSIMILARITY PROJECT>
Step 3 — Run the program
Use:
python .\evidence_tracker.py
Press Enter.
The program should load the evidence dataset and display the evidence
review information.
Step 4 — Check the output
The program should display information such as:
- Candidate product
- Evidence categories
- Number of evidence records
- Validation status
- Evidence limitations
- Evidence gaps
- Structured JSON output
7. CSV Dataset Description
The sample dataset is stored at:
sample_data/candidate_evidence.csv
The CSV file contains synthetic evidence records for software testing.
The main fields are:
- Evidence ID
- Reference Product
- Candidate Product
- Evidence Category
- Study/Source
- Measurement
- Result
- Control
- Evidence Quality
- Validation Status
- Limitation
- Reviewer Note
The records are clearly identified as:
SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING
They are not published experimental results.
8. Features of the Evidence Tracker
The Python Evidence Tracker is designed to:
1. Load the CSV evidence dataset.
2. Search by reference product.
3. Search by candidate product.
4. Filter evidence by evidence category.
5. Filter evidence by validation status.
6. Display evidence records.
7. Display evidence limitations.
8. Identify incomplete evidence.
9. Compare reference and candidate evidence records.
10. Produce structured JSON output.
The tracker is intended to organize evidence and highlight information
that may require further review.
9. Example Output
A simplified example of the intended review output is:
Biosimilarity Evidence Review

Candidate:
Candidate-B

Evidence Categories:
Analytical
Functional
Preclinical

Evidence Records:
8

Verified:
5

Needs Review:
2

Insufficient:
1

Known Evidence Gaps:
Immunogenicity data incomplete
The actual output depends on the evidence records present in the CSV
dataset.
The program can also produce structured JSON output for the evidence
records.
10. Testing
The project includes testing of normal inputs, invalid inputs, and
evidence-quality edge cases.
The tests cover:
Normal test cases
- Valid candidate search
- Evidence category filtering
- Validation status filtering
- Evidence record display
- JSON output generation
Invalid-input cases
- Unknown candidate
- Missing evidence ID
- Duplicate evidence ID
- Invalid evidence status
Evidence-quality and other edge cases
- Incomplete study record
- Conflicting evidence
- Empty dataset
- Malformed CSV
- Comparison with missing evidence categories
Testing results are documented in:
tests/TEST_RESULTS.md
Each test records:
- Expected result
- Actual result
- Pass/Fail status
11. Important Scientific Disclaimer
This is an evidence-organisation tool, not a regulatory approval system.
This project does not:
- Approve biosimilar products.
- Determine clinical efficacy.
- Determine clinical safety.
- Replace regulatory assessment.
- Replace expert scientific review.
- Make therapeutic decisions.
- Establish that a candidate product is biosimilar.
- Replace laboratory, clinical, or regulatory evidence.
The evidence tracker is an organizational and educational tool.
12. Limitations
The project has the following limitations:
1. The sample dataset contains synthetic records.
2. The dataset is small and is intended for software testing.
3. The tracker does not independently verify scientific claims.
4. The tracker does not perform regulatory assessment.
5. Evidence-quality statuses are organizational classifications.
6. The tracker does not establish biosimilarity.
7. The tracker does not establish clinical equivalence.
8. The tracker does not replace expert scientific judgment.
9. The quality of the output depends on the quality and completeness of
   the input CSV.
10. Missing or conflicting evidence requires human review.
13. Responsible Use
The project should be used for educational purposes and evidence
organization.
Scientific interpretation, regulatory assessment, clinical decisions,
and research decisions must be performed by appropriately qualified
human reviewers.
A classification such as VERIFIED, PARTIAL, NEEDS REVIEW,
CONFLICTING, or INSUFFICIENT should not by itself be interpreted as
a scientific or regulatory conclusion.
14. Project Workflow
The overall workflow used in this project is:
Learn
  ↓
Research
  ↓
Build Evidence Map
  ↓
Create QC Model
  ↓
Create Synthetic Evidence Dataset
  ↓
Build Python Evidence Tracker
  ↓
Test
  ↓
Document
  ↓
Human Review
15. Conclusion
This project establishes a basic, traceable framework for organizing
biosimilarity and preclinical evidence.
The Python mini-build demonstrates how structured evidence records can
be loaded, searched, filtered, reviewed, compared, and represented as
JSON.
The project is intended to provide a foundation that can be extended by
future research, QA/QC, laboratory, AI/data-science, software, and
regulatory research teams.

