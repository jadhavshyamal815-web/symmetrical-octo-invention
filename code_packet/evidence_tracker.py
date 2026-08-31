import csv
import json
from pathlib import Path


def safe_input(prompt=""):
    """Safely read user input without crashing when stdin is unavailable."""
    try:
        return input(prompt).strip()
    except EOFError:
        return ""


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
FRAMEWORK_DIR = BASE_DIR / "evidence_framework"

EVIDENCE_FILE = FRAMEWORK_DIR / "evidence_map.csv"
CLAIM_FILE = FRAMEWORK_DIR / "claim_traceability.csv"
CONTRADICTION_FILE = FRAMEWORK_DIR / "contradiction_register.csv"

OUTPUT_FILE = BASE_DIR / "sample_implementation" / "sample_output.json"


def load_csv(file_path):
    """Load a CSV file and return its records."""
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def show_evidence(records):
    """Display evidence records."""
    print("\n=== EVIDENCE RECORDS ===")

    for record in records:
        evidence_id = record.get("evidence_id", "")
        title = (
            record.get("title")
            or record.get("evidence_title")
            or record.get("claim")
            or record.get("description")
            or ""
        )
        category = record.get("category", "")
        status = (
            record.get("validation_status")
            or record.get("status")
            or record.get("evidence_status")
            or ""
        )

        print(
            f"{evidence_id} | {title} | {category} | {status}"
        )


def find_evidence(records, evidence_id):
    """Find one evidence record by ID."""
    for record in records:
        if record.get("evidence_id", "").strip().upper() == evidence_id.upper():
            return record

    return None


def filter_by_category(records, category):
    """Filter evidence records by category."""
    if not category:
        return records

    return [
        record
        for record in records
        if record.get("category", "").strip().upper()
        == category.upper()
    ]


def build_output(evidence_records, claim_records, contradiction_records):
    """Build structured JSON output."""
    incomplete = []

    for record in evidence_records:
        status = (
            record.get("validation_status")
            or record.get("status")
            or record.get("evidence_status")
            or ""
        ).strip().upper()

        if status in {
            "INSUFFICIENT",
            "NEEDS REVIEW",
            "PARTIAL",
            "CONFLICTING",
        }:
            incomplete.append(record.get("evidence_id", ""))

    return {
        "tracker": "Scientific Evidence Tracker",
        "evidence_records_loaded": len(evidence_records),
        "claim_records_loaded": len(claim_records),
        "contradiction_records_loaded": len(contradiction_records),
        "incomplete_evidence_ids": incomplete,
        "evidence_records": evidence_records,
    }


def save_output(data):
    """Save tracker output as JSON."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main():
    print("Scientific Evidence Tracker")
    print("============================")

    # Check required files
    required_files = [
        EVIDENCE_FILE,
        CLAIM_FILE,
        CONTRADICTION_FILE,
    ]

    for file_path in required_files:
        if not file_path.exists():
            print("\nERROR: Required file not found.")
            print(file_path)
            return 1

    # Load CSV files
    evidence_records = load_csv(EVIDENCE_FILE)
    claim_records = load_csv(CLAIM_FILE)
    contradiction_records = load_csv(CONTRADICTION_FILE)

    print(f"\nEvidence records loaded: {len(evidence_records)}")
    print(f"Claim records loaded: {len(claim_records)}")
    print(
        f"Contradiction records loaded: "
        f"{len(contradiction_records)}"
    )

    # Display all evidence
    show_evidence(evidence_records)

    # Evidence ID inspection
    evidence_id = safe_input(
        "\nEnter an evidence ID to inspect "
        "(example: EV-004, or press Enter to skip): "
    )

    if evidence_id:
        record = find_evidence(evidence_records, evidence_id)

        if record:
            print("\n=== SELECTED EVIDENCE ===")
            print(json.dumps(record, indent=2, ensure_ascii=False))
        else:
            print("\nEvidence ID not found.")

    # Category filter
    category = safe_input(
        "\nEnter evidence category to filter "
        "(example: META-ANALYSIS, or press Enter to skip): "
    )

    filtered_records = filter_by_category(
        evidence_records,
        category
    )

    if category:
        print(f"\n=== CATEGORY: {category} ===")
        show_evidence(filtered_records)

    # Build and save output
    output_data = build_output(
        evidence_records,
        claim_records,
        contradiction_records,
    )

    save_output(output_data)

    print("\n=== OUTPUT ===")
    print(f"JSON output saved to: {OUTPUT_FILE}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())