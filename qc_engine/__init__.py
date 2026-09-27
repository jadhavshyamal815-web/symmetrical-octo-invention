"""BHIV Biotech Evidence QC Engine."""

from .engine import (
    ENGINE_VERSION,
    SCHEMA_VERSION,
    classify_record,
    compare_candidate_reference,
    completeness,
    detect_conflicts,
    detect_duplicates,
    human_review_required,
    process_dataset,
    validate_record,
)

__all__ = [
    "ENGINE_VERSION",
    "SCHEMA_VERSION",
    "classify_record",
    "compare_candidate_reference",
    "completeness",
    "detect_conflicts",
    "detect_duplicates",
    "human_review_required",
    "process_dataset",
    "validate_record",
]