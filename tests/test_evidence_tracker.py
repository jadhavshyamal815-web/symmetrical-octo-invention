import pytest
from pathlib import Path
import csv
import json
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
EVIDENCE_FILE = ROOT / "evidence_framework" / "evidence_map.csv"
CLAIM_FILE = ROOT / "evidence_framework" / "claim_traceability.csv"
CONTRADICTION_FILE = ROOT / "evidence_framework" / "contradiction_register.csv"
TRACKER = ROOT / "code_packet" / "evidence_tracker.py"
OUTPUT_FILE = ROOT / "sample_implementation" / "sample_output.json"


# ---------- Normal tests ----------

def test_evidence_file_exists():
    assert EVIDENCE_FILE.exists()


def test_claim_file_exists():
    assert CLAIM_FILE.exists()


def test_contradiction_file_exists():
    assert CONTRADICTION_FILE.exists()


def test_evidence_records_are_loaded():
    with open(EVIDENCE_FILE, encoding="utf-8-sig", newline="") as f:
        records = list(csv.DictReader(f))

    assert len(records) > 0


def test_tracker_script_exists():
    assert TRACKER.exists()


# ---------- Invalid-input / edge tests ----------

def test_unknown_evidence_id():
    with open(EVIDENCE_FILE, encoding="utf-8-sig", newline="") as f:
        records = list(csv.DictReader(f))

    evidence_ids = {
        row.get("evidence_id", "").strip()
        for row in records
    }

    assert "EV-999" not in evidence_ids


def test_evidence_records_have_ids():
    with open(EVIDENCE_FILE, encoding="utf-8-sig", newline="") as f:
        records = list(csv.DictReader(f))

    assert all(row.get("evidence_id", "").strip() for row in records)


def test_evidence_dataset_is_not_empty():
    with open(EVIDENCE_FILE, encoding="utf-8-sig", newline="") as f:
        records = list(csv.DictReader(f))

    assert records != []


# ---------- Output validation ----------

def test_tracker_output_json_exists_after_run():
    result = subprocess.run(
        [sys.executable, str(TRACKER)],
        input="\n",
        text=True,
        capture_output=True,
        cwd=ROOT
    )

    assert result.returncode == 0
    assert OUTPUT_FILE.exists()


def test_output_json_is_valid():
    if not OUTPUT_FILE.exists():
        pytest.skip("Output JSON has not been generated yet")

    with open(OUTPUT_FILE, encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, dict)