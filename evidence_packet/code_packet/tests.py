import copy

from qc_engine.engine import (
    classify_record,
    detect_conflicts,
    detect_duplicates,
    human_review_required,
    process_dataset,
    validate_record,
)


def make_complete_record():
    return {
        "schema_version": "1.0.0",
        "evidence_id": "TEST-EVID-001",
        "study_id": "TEST-STUDY-001",
        "source": "Synthetic Test Source",
        "protocol_reference": "TEST-PROTOCOL-001",
        "sample_identification": "Synthetic Candidate",
        "control_identification": "Synthetic Reference",
        "experimental_conditions": "Synthetic controlled condition",
        "measurement_method": "Synthetic validated assay",
        "method_validation_status": "VALIDATED",
        "raw_data_availability": "AVAILABLE",
        "missing_data": [],
        "deviations": [],
        "statistical_reporting": "Reported",
        "reproducibility": "Reported",
        "limitations": "Synthetic software test",
        "evidence_category": "Preclinical",
        "synthetic_data_declaration": (
            "SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING"
        ),
        "reviewer_status": "NOT REVIEWED",
        "evidence_quality": "VERIFIED",
        "final_review_status": "OPEN",
    }


def test_qc_001_complete_verified():
    record = make_complete_record()

    result = classify_record(record)

    assert result["evidence_quality"] == "VERIFIED"
    assert result["validation"]["valid"] is True
    assert result["completeness"]["complete"] is True


def test_qc_002_missing_raw_partial_review():
    record = make_complete_record()

    record["raw_data_availability"] = "NOT_AVAILABLE"
    record["missing_data"] = ["Raw data unavailable"]

    result = classify_record(record)

    assert result["evidence_quality"] == "PARTIAL"

    assert human_review_required(
        result,
        record,
    ) is True


def test_qc_003_missing_source():
    record = make_complete_record()

    record["source"] = ""

    result = classify_record(record)

    assert result["completeness"]["complete"] is False
    assert result["evidence_quality"] == "INSUFFICIENT"


def test_qc_004_conflict():
    record_a = make_complete_record()
    record_b = make_complete_record()

    record_a["evidence_id"] = "TEST-EVID-004-A"
    record_b["evidence_id"] = "TEST-EVID-004-B"

    record_a["study_id"] = "TEST-STUDY-004"
    record_b["study_id"] = "TEST-STUDY-004"

    record_a["measurement_method"] = "Method A"
    record_b["measurement_method"] = "Method B"

    conflicts = detect_conflicts(
        [record_a, record_b]
    )

    assert len(conflicts) > 0
    assert conflicts[0]["study_id"] == "TEST-STUDY-004"


def test_qc_005_missing_method():
    record = make_complete_record()

    record["measurement_method"] = ""
    record["method_validation_status"] = "NOT_REPORTED"

    result = classify_record(record)

    assert result["completeness"]["complete"] is False
    assert result["evidence_quality"] == "INSUFFICIENT"


def test_qc_006_missing_study_id():
    record = make_complete_record()

    record["study_id"] = ""

    result = classify_record(record)

    assert result["completeness"]["complete"] is False
    assert result["evidence_quality"] == "INSUFFICIENT"


def test_qc_007_duplicate_id():
    record_a = make_complete_record()
    record_b = make_complete_record()

    record_a["evidence_id"] = "DUPLICATE-ID"
    record_b["evidence_id"] = "DUPLICATE-ID"

    duplicates = detect_duplicates(
        [record_a, record_b]
    )

    assert len(duplicates) > 0

    assert any(
        item["type"] == "DUPLICATE_EVIDENCE_ID"
        for item in duplicates
    )


def test_qc_008_invalid_status_rejected():
    record = make_complete_record()

    record["reviewer_status"] = "INVALID STATUS"

    validation = validate_record(record)

    assert validation["valid"] is False

    assert any(
        "reviewer_status" in error
        for error in validation["errors"]
    )


def test_qc_009_empty_dataset():
    result = process_dataset([])

    assert result["record_count"] == 0
    assert result["results"] == []
    assert result["duplicates"] == []
    assert result["conflicts"] == []


def test_qc_010_missing_category():
    record = make_complete_record()

    record["evidence_category"] = ""

    result = classify_record(record)

    assert result["completeness"]["complete"] is False
    assert result["evidence_quality"] == "INSUFFICIENT"


def test_repeatability():
    dataset = [
        make_complete_record()
    ]

    first = process_dataset(
        copy.deepcopy(dataset)
    )

    second = process_dataset(
        copy.deepcopy(dataset)
    )

    assert first == second


def test_synthetic_label_preserved():
    record = make_complete_record()

    result = process_dataset([record])

    assert (
        result["results"][0]["synthetic_data_declaration"]
        == "SAMPLE / SYNTHETIC / FOR SOFTWARE TESTING"
    )


def test_human_review_required_for_partial():
    record = make_complete_record()

    record["raw_data_availability"] = "PARTIAL"

    classification = classify_record(record)

    assert classification["evidence_quality"] == "PARTIAL"

    assert human_review_required(
        classification,
        record,
    ) is True


def test_scientific_conclusion_is_not_created():
    record = make_complete_record()

    result = process_dataset([record])

    assert result["scientific_conclusion"] is None