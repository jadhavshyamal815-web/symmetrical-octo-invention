# Phase 8 — Testing

## Purpose

Testing was performed to evaluate the Biosimilarity Evidence Tracker
against normal, invalid-input, and evidence-quality scenarios.

The test dataset is synthetic and is intended only for software testing.

---

## Test Results

| Test ID | Test Case | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC-01 | Valid candidate search | Existing candidate records displayed | Candidate-B records displayed | PASS |
| TC-02 | Unknown candidate | No evidence records found | No records found | PASS |
| TC-03 | Evidence category filter | Analytical records displayed | Analytical records displayed | PASS |
| TC-04 | Validation status filter | VERIFIED records displayed | VERIFIED records displayed | PASS |
| TC-05 | JSON output | Structured JSON generated | JSON generated successfully | PASS |
| TC-06 | Missing Evidence ID | Missing ID identified | Record loaded without automatic ID validation | FAIL / NEEDS IMPROVEMENT |
| TC-07 | Duplicate Evidence ID | Duplicate ID identified | Duplicate not automatically detected | FAIL / NEEDS IMPROVEMENT |
| TC-08 | Invalid evidence status | Invalid status rejected/flagged | Record loaded without status validation | FAIL / NEEDS IMPROVEMENT |
| TC-09 | Incomplete study record | Incomplete evidence identified | Record flagged/reviewed | PASS |
| TC-10 | Conflicting evidence | Conflict identified for human review | Conflict requires review | PASS |
## Test Case Details

### TC-01 — Valid Candidate Search

Input:
Candidate-B

Expected:
Evidence records associated with Candidate-B should be displayed.

Actual:
Candidate-B evidence records were displayed.

Result:
PASS


### TC-02 — Unknown Candidate

Input:
Candidate-XYZ

Expected:
No evidence records should be found.

Actual:
No evidence records were found.

Result:
PASS


### TC-03 — Evidence Category Filter

Input:
Analytical

Expected:
Only analytical evidence records should be displayed.

Actual:
Analytical evidence records were displayed.

Result:
PASS


### TC-04 — Validation Status Filter

Input:
VERIFIED

Expected:
Only VERIFIED records should be returned.

Actual:
VERIFIED records were displayed.

Result:
PASS


### TC-05 — JSON Output

Input:
Candidate-B

Expected:
Structured JSON output should be generated.

Actual:
Structured JSON output was generated.

Result:
PASS


### TC-06 — Missing Evidence ID

Input:
A synthetic record with a missing Evidence ID.

Expected:
The incomplete record should be detected.

Actual:
[Write your actual result here.]

Result:
[PASS/FAIL]


### TC-07 — Duplicate Evidence ID

Input:
Two records with the same Evidence ID.

Expected:
Duplicate Evidence ID should be identified.

Actual:
[Write your actual result here.]

Result:
[PASS/FAIL]


### TC-08 — Invalid Evidence Status

Input:
Invalid status such as APPROVED.

Expected:
Invalid status should be rejected or flagged.

Actual:
[Write your actual result here.]

Result:
[PASS/FAIL]


### TC-09 — Incomplete Study Record

Input:
Record with missing study/source or measurement information.

Expected:
Incomplete evidence should be identified.

Actual:
[Write your actual result here.]

Result:
[PASS/FAIL]


### TC-10 — Conflicting Evidence

Input:
Two synthetic evidence records with conflicting results.

Expected:
Conflict should require human review rather than an automatic scientific conclusion.

Actual:
[Write your actual result here.]

Result:
[PASS/FAIL]