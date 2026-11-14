
import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_PATH = ROOT / "schemas" / "evidence_qc_schema_v1.0.0.json"
DATA_PATH = ROOT / "data" / "synthetic_evidence.json"


def load_schema_and_data():
    with open(SCHEMA_PATH, encoding="utf-8") as file:
        schema = json.load(file)

    with open(DATA_PATH, encoding="utf-8") as file:
        records = json.load(file)

    return schema, records


def test_json_schema_is_valid():
    schema, _ = load_schema_and_data()
    Draft202012Validator.check_schema(schema)


def test_complete_records_pass_schema_validation():
    schema, records = load_schema_and_data()
    validator = Draft202012Validator(schema)

    expected_invalid_ids = {
        "EVID-QC-003",
        "EVID-QC-005",
        "EVID-QC-006",
        "EVID-QC-008",
        "EVID-QC-010",
    }

    for record in records:
        errors = list(validator.iter_errors(record))

        if record["evidence_id"] in expected_invalid_ids:
            assert errors, (
                f"{record['evidence_id']} should fail schema validation"
            )
        else:
            assert not errors, (
                f"{record['evidence_id']} unexpectedly failed: "
                + "; ".join(error.message for error in errors)
            )


def test_expected_invalid_records_are_detected():
    schema, records = load_schema_and_data()
    validator = Draft202012Validator(schema)

    expected_invalid_ids = {
        "EVID-QC-003",
        "EVID-QC-005",
        "EVID-QC-006",
        "EVID-QC-008",
        "EVID-QC-010",
    }

    detected_invalid_ids = {
        record["evidence_id"]
        for record in records
        if list(validator.iter_errors(record))
    }

    assert detected_invalid_ids == expected_invalid_ids

