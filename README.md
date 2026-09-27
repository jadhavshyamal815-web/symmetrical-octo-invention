# BHIV Biosimilarity & Preclinical Evidence QC Engine

## Version

1.0.0

## Purpose

This project implements a deterministic quality-control engine for structured biosimilarity and preclinical evidence records.

The engine performs:

- schema-aligned record validation
- required-field checks
- evidence completeness checks
- duplicate detection
- conflict detection
- evidence-quality classification
- human-review routing
- candidate/reference field comparison
- synthetic-data protection
- deterministic repeatability testing

## Scientific Boundary

The engine does NOT determine:

- biosimilarity
- clinical equivalence
- interchangeability
- safety
- efficacy
- regulatory approval
- therapeutic effectiveness

The output is a QC classification and review-routing result only.

## Versioned Components

- Engine version: `1.0.0`
- Schema version: `1.0.0`

## Evidence Quality States

- VERIFIED
- PARTIAL
- NEEDS REVIEW
- CONFLICTING
- INSUFFICIENT

## Reviewer Status

- NOT REVIEWED
- IN REVIEW
- REVIEWED
- REQUIRES SECOND REVIEW
- CLOSED

## Final Review Status

- OPEN
- IN REVIEW
- REQUIRES REVISION
- READY FOR HUMAN REVIEW
- REVIEWED
- CLOSED

## Synthetic Data

The included dataset is explicitly labelled:

`SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING`

It must not be interpreted as real scientific evidence.

## Running the Engine

Activate the virtual environment and run:

```powershell
python qc_engine\engine.py data\synthetic_evidence.json -o evidence_packet\api_samples\qc_output.json