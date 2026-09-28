"""
BHIV Biotech - Biosimilarity & Preclinical Evidence QC Engine

Version: 1.0.0

Purpose:
    Deterministic quality-control processing for biosimilarity and
    preclinical evidence records.

Important boundary:
    This engine does NOT establish biosimilarity, clinical equivalence,
    interchangeability, safety, efficacy, or regulatory validity.

Synthetic records must remain explicitly labelled as synthetic.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ENGINE_VERSION = "1.0.0"
SCHEMA_VERSION = "1.0.0"

EVIDENCE_QUALITY_STATES = {
    "VERIFIED",
    "PARTIAL",
    "NEEDS REVIEW",
    "CONFLICTING",
    "INSUFFICIENT",
}

REVIEWER_STATES = {
    "NOT REVIEWED",
    "IN REVIEW",
    "REVIEWED",
    "REQUIRES SECOND REVIEW",
    "CLOSED",
}

FINAL_REVIEW_STATES = {
    "OPEN",
    "IN REVIEW",
    "REQUIRES REVISION",
    "READY FOR HUMAN REVIEW",
    "REVIEWED",
    "CLOSED",
}

METHOD_VALIDATION_STATES = {
    "VALIDATED",
    "PARTIALLY_VALIDATED",
    "NOT_VALIDATED",
    "NOT_REPORTED",
}

RAW_DATA_STATES = {
    "AVAILABLE",
    "NOT_AVAILABLE",
    "PARTIAL",
    "NOT_REPORTED",
}

SYNTHETIC_DECLARATIONS = {
    "SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING",
    "REAL / SOURCE-VERIFIED",
}

REQUIRED_FIELDS = [
    "schema_version",
    "evidence_id",
    "study_id",
    "source",
    "protocol_reference",
    "sample_identification",
    "control_identification",
    "experimental_conditions",
    "measurement_method",
    "method_validation_status",
    "raw_data_availability",
    "missing_data",
    "deviations",
    "statistical_reporting",
    "reproducibility",
    "limitations",
    "evidence_category",
    "synthetic_data_declaration",
    "reviewer_status",
    "evidence_quality",
    "final_review_status",
]

CONTENT_FIELDS = [
    "study_id",
    "source",
    "protocol_reference",
    "sample_identification",
    "control_identification",
    "experimental_conditions",
    "measurement_method",
    "statistical_reporting",
    "reproducibility",
    "limitations",
    "evidence_category",
]


def _blank(value: Any) -> bool:
    """Return True when a value is missing or blank."""
    return value is None or value == ""


def validate_record(record: dict[str, Any]) -> dict[str, Any]:
    """
    Validate one evidence record.

    Returns structured validation information without making
    scientific conclusions.
    """
    errors: list[str] = []

    if not isinstance(record, dict):
        return {
            "valid": False,
            "errors": ["Record must be a JSON object."],
        }

    for field in REQUIRED_FIELDS:
        if field not in record:
            errors.append(f"Missing required field: {field}")

    if record.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {SCHEMA_VERSION}"
        )

    if "method_validation_status" in record:
        if record["method_validation_status"] not in METHOD_VALIDATION_STATES:
            errors.append("Invalid method_validation_status")

    if "raw_data_availability" in record:
        if record["raw_data_availability"] not in RAW_DATA_STATES:
            errors.append("Invalid raw_data_availability")

    if "synthetic_data_declaration" in record:
        if record["synthetic_data_declaration"] not in SYNTHETIC_DECLARATIONS:
            errors.append("Invalid synthetic_data_declaration")

    if "reviewer_status" in record:
        if record["reviewer_status"] not in REVIEWER_STATES:
            errors.append("Invalid reviewer_status")

    if "evidence_quality" in record:
        if record["evidence_quality"] not in EVIDENCE_QUALITY_STATES:
            errors.append("Invalid evidence_quality")

    if "final_review_status" in record:
        if record["final_review_status"] not in FINAL_REVIEW_STATES:
            errors.append("Invalid final_review_status")

    if "missing_data" in record and not isinstance(
        record["missing_data"], list
    ):
        errors.append("missing_data must be a list")

    if "deviations" in record and not isinstance(
        record["deviations"], list
    ):
        errors.append("deviations must be a list")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }


def completeness(record: dict[str, Any]) -> dict[str, Any]:
    """
    Check structural/content completeness.

    Empty missing_data and deviations lists are valid because an
    empty list can explicitly mean that no missing data/deviations
    were reported.
    """
    checks: dict[str, bool] = {}

    for field in CONTENT_FIELDS:
        checks[field] = (
            record.get(field) is not None
            and record.get(field) != ""
            and (
                field in {"missing_data", "deviations"}
                or record.get(field) != []
            )
        )

    checks["method_validation_status"] = (
        record.get("method_validation_status") in METHOD_VALIDATION_STATES
    )

    checks["raw_data_availability"] = (
        record.get("raw_data_availability") in RAW_DATA_STATES
    )

    checks["statistical_reporting"] = not _blank(
        record.get("statistical_reporting")
    )

    checks["reproducibility"] = not _blank(
        record.get("reproducibility")
    )

    checks["limitations"] = not _blank(
        record.get("limitations")
    )

    checks["synthetic_data_declaration"] = (
        record.get("synthetic_data_declaration")
        in SYNTHETIC_DECLARATIONS
    )

    missing_fields = [
        field for field, passed in checks.items() if not passed
    ]

    return {
        "complete": len(missing_fields) == 0,
        "checks": checks,
        "missing_fields": missing_fields,
    }


def detect_duplicates(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Detect duplicate evidence_id and study_id values."""
    duplicates: list[dict[str, Any]] = []

    seen_evidence: dict[str, int] = {}
    seen_studies: dict[str, int] = {}

    for index, record in enumerate(records):
        evidence_id = record.get("evidence_id")
        study_id = record.get("study_id")

        if evidence_id:
            if evidence_id in seen_evidence:
                duplicates.append(
                    {
                        "type": "DUPLICATE_EVIDENCE_ID",
                        "value": evidence_id,
                        "first_index": seen_evidence[evidence_id],
                        "duplicate_index": index,
                    }
                )
            else:
                seen_evidence[evidence_id] = index

        if study_id:
            if study_id in seen_studies:
                duplicates.append(
                    {
                        "type": "DUPLICATE_STUDY_ID",
                        "value": study_id,
                        "first_index": seen_studies[study_id],
                        "duplicate_index": index,
                    }
                )
            else:
                seen_studies[study_id] = index

    return duplicates


def detect_conflicts(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Detect inconsistent values for records representing the same study.

    Conflicts are preserved and flagged. They are not silently resolved.
    """
    conflicts: list[dict[str, Any]] = []

    grouped: dict[str, list[tuple[int, dict[str, Any]]]] = {}

    for index, record in enumerate(records):
        study_id = record.get("study_id")

        if study_id:
            grouped.setdefault(study_id, []).append(
                (index, record)
            )

    conflict_fields = [
        "measurement_method",
        "control_identification",
        "evidence_quality",
        "statistical_reporting",
    ]

    for study_id, group in grouped.items():
        if len(group) < 2:
            continue

        for field in conflict_fields:
            values = []

            for index, record in group:
                value = record.get(field)

                if value is not None:
                    values.append(
                        {
                            "index": index,
                            "value": value,
                        }
                    )

            unique_values = sorted(
                {
                    str(item["value"])
                    for item in values
                }
            )

            if len(unique_values) > 1:
                conflicts.append(
                    {
                        "type": "CONFLICTING_FIELD",
                        "study_id": study_id,
                        "field": field,
                        "values": values,
                    }
                )

    return conflicts


def classify_record(
    record: dict[str, Any],
    duplicate_ids: set[str] | None = None,
    conflict_study_ids: set[str] | None = None,
) -> dict[str, Any]:
    """
    Deterministically classify one record.

    This is a QC classification only. It is not a scientific conclusion.
    """
    duplicate_ids = duplicate_ids or set()
    conflict_study_ids = conflict_study_ids or set()

    validation = validate_record(record)
    completeness_result = completeness(record)

    evidence_id = record.get("evidence_id")
    study_id = record.get("study_id")

    if not validation["valid"]:
        quality = "INSUFFICIENT"
        reason = "Record failed structural or state validation."

    elif study_id in conflict_study_ids:
        quality = "CONFLICTING"
        reason = "Conflicting values were detected for the study."

    elif evidence_id in duplicate_ids:
        quality = "NEEDS REVIEW"
        reason = "Duplicate evidence identifier detected."

    elif not completeness_result["complete"]:
        quality = "INSUFFICIENT"
        reason = "Required evidence information is incomplete."

    elif record.get("raw_data_availability") in {
        "NOT_AVAILABLE",
        "PARTIAL",
        "NOT_REPORTED",
    }:
        quality = "PARTIAL"
        reason = "Raw-data availability is incomplete."

    elif record.get("method_validation_status") in {
        "NOT_VALIDATED",
        "NOT_REPORTED",
    }:
        quality = "NEEDS REVIEW"
        reason = "Measurement method validation is incomplete."

    elif record.get("method_validation_status") == "PARTIALLY_VALIDATED":
        quality = "PARTIAL"
        reason = "Measurement method is only partially validated."

    else:
        quality = "VERIFIED"
        reason = "Required QC fields are structurally complete."

    return {
        "evidence_quality": quality,
        "reason": reason,
        "validation": validation,
        "completeness": completeness_result,
    }


def human_review_required(
    classification: dict[str, Any],
    record: dict[str, Any],
) -> bool:
    """Determine whether human review is required."""
    quality = classification["evidence_quality"]

    if quality in {
        "PARTIAL",
        "NEEDS REVIEW",
        "CONFLICTING",
        "INSUFFICIENT",
    }:
        return True

    if record.get("reviewer_status") in {
        "NOT REVIEWED",
        "IN REVIEW",
        "REQUIRES SECOND REVIEW",
    }:
        return True

    if record.get("final_review_status") in {
        "OPEN",
        "IN REVIEW",
        "REQUIRES REVISION",
        "READY FOR HUMAN REVIEW",
    }:
        return True

    return False


def process_dataset(records: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Process a complete evidence dataset and return deterministic JSON.
    """
    if not isinstance(records, list):
        raise TypeError("Dataset must be a list of evidence records.")

    duplicates = detect_duplicates(records)
    conflicts = detect_conflicts(records)

    duplicate_evidence_ids = {
        item["value"]
        for item in duplicates
        if item["type"] == "DUPLICATE_EVIDENCE_ID"
    }

    conflict_study_ids = {
        item["study_id"]
        for item in conflicts
    }

    results = []

    for index, record in enumerate(records):
        classification = classify_record(
            record,
            duplicate_ids=duplicate_evidence_ids,
            conflict_study_ids=conflict_study_ids,
        )

        review_required = human_review_required(
            classification,
            record,
        )

        results.append(
            {
                "index": index,
                "evidence_id": record.get("evidence_id"),
                "study_id": record.get("study_id"),
                "evidence_quality": classification["evidence_quality"],
                "reason": classification["reason"],
                "human_review_required": review_required,
                "validation": classification["validation"],
                "completeness": classification["completeness"],
                "synthetic_data_declaration": record.get(
                    "synthetic_data_declaration"
                ),
                "reviewer_status": record.get("reviewer_status"),
                "final_review_status": record.get(
                    "final_review_status"
                ),
            }
        )

    return {
        "engine_version": ENGINE_VERSION,
        "schema_version": SCHEMA_VERSION,
        "record_count": len(records),
        "duplicates": duplicates,
        "conflicts": conflicts,
        "results": results,
        "human_review_required_count": sum(
            1
            for item in results
            if item["human_review_required"]
        ),
        "scientific_conclusion": None,
    }


def compare_candidate_reference(
    candidate: dict[str, Any],
    reference: dict[str, Any],
) -> dict[str, Any]:
    """
    Compare candidate/reference fields without making a scientific conclusion.
    """
    fields = [
        "sample_identification",
        "control_identification",
        "experimental_conditions",
        "measurement_method",
        "method_validation_status",
        "raw_data_availability",
        "statistical_reporting",
        "reproducibility",
        "limitations",
    ]

    comparison = {}

    for field in fields:
        comparison[field] = {
            "candidate": candidate.get(field),
            "reference": reference.get(field),
            "match": candidate.get(field) == reference.get(field),
        }

    return {
        "candidate_evidence_id": candidate.get("evidence_id"),
        "reference_evidence_id": reference.get("evidence_id"),
        "comparison": comparison,
        "scientific_conclusion": None,
        "human_review_required": True,
    }


def load_json(path: str | Path) -> Any:
    """Load JSON from disk."""
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: str | Path, data: Any) -> None:
    """Write deterministic formatted JSON."""
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(
            data,
            handle,
            indent=2,
            sort_keys=True,
        )
        handle.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="BHIV Biosimilarity & Preclinical Evidence QC Engine"
    )

    parser.add_argument(
        "input",
        help="Path to evidence JSON dataset",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="qc_output.json",
        help="Output JSON path",
    )

    args = parser.parse_args()

    records = load_json(args.input)

    if not isinstance(records, list):
        raise SystemExit(
            "Input JSON must contain an array of evidence records."
        )

    output = process_dataset(records)

    write_json(args.output, output)

    print(
        f"QC processing complete: {len(records)} record(s)"
    )

    print(
        f"Output written to: {args.output}"
    )


if __name__ == "__main__":
    main()