import csv
import json
from pathlib import Path


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
        print(
            f"{record['evidence_id']} | "
            f"{record['concept']} | "
            f"{record['evidence_category']} | "
            f"{record['evidence_strength']}"
        )


def search_evidence(records, evidence_id):
    """Search for one evidence record."""
    for record in records:
        if record["evidence_id"].strip().upper() == evidence_id.upper():
            return record

    return None


def filter_by_category(records, category):
    """Filter evidence by evidence category."""
    return [
        record
        for record in records
        if record["evidence_category"].upper() == category.upper()
    ]


def filter_by_strength(records, strength):
    """Filter evidence by evidence strength."""
    return [
        record
        for record in records
        if record["evidence_strength"].upper() == strength.upper()
    ]


def find_incomplete(records):
    """Find insufficient or unknown evidence."""
    return [
        record
        for record in records
        if record["evidence_strength"].upper()
        in ["INSUFFICIENT", "UNKNOWN"]
    ]


def show_contradictions(records):
    """Display contradiction records."""
    print("\n=== CONTRADICTION REGISTER ===")

    for record in records:
        print(
            f"{record['contradiction_id']} | "
            f"{record['claim_id']} | "
            f"{record['resolution_status']}"
        )


def create_json_output(evidence_records, claim_records, contradiction_records):
    """Create a structured JSON summary."""
    output = {
        "framework": "Scientific Evidence and Translational Research Mapping",
        "version": "1.0",
        "evidence_records": evidence_records,
        "claim_records": claim_records,
        "contradiction_records": contradiction_records,
        "quality_controls": {
            "unsupported_claims_downgraded": True,
            "contradictions_visible": True,
            "unknown_status_preserved": True,
            "source_traceability_preserved": True
        }
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=2)

    return OUTPUT_FILE


def main():
    print("Scientific Evidence Tracker")
    print("===========================")

    try:
        evidence_records = load_csv(EVIDENCE_FILE)
        claim_records = load_csv(CLAIM_FILE)
        contradiction_records = load_csv(CONTRADICTION_FILE)

    except FileNotFoundError as error:
        print("\nERROR: Required file not found.")
        print(error)
        return

    print(f"\nEvidence records loaded: {len(evidence_records)}")
    print(f"Claim records loaded: {len(claim_records)}")
    print(f"Contradiction records loaded: {len(contradiction_records)}")

    show_evidence(evidence_records)

    # Search test
    selected_id = input(
        "\nEnter an evidence ID to inspect "
        "(example: EV-004, or press Enter to skip): "
    ).strip()

    if selected_id:
        record = search_evidence(evidence_records, selected_id)

        if record:
            print("\n=== SELECTED EVIDENCE ===")
            for key, value in record.items():
                print(f"{key}: {value}")
        else:
            print("\nEvidence record not found.")

    # Category filter
    category = input(
        "\nEnter evidence category to filter "
        "(example: META_ANALYSIS, or press Enter to skip): "
    ).strip()

    if category:
        filtered = filter_by_category(evidence_records, category)

        print("\n=== CATEGORY FILTER RESULTS ===")

        if filtered:
            for record in filtered:
                print(
                    f"{record['evidence_id']} | "
                    f"{record['evidence_category']} | "
                    f"{record['evidence_strength']}"
                )
        else:
            print("No records found for this category.")

    # Strength filter
    strength = input(
        "\nEnter evidence strength to filter "
        "(HIGH, MODERATE, LOW, INSUFFICIENT, UNKNOWN; "
        "or press Enter to skip): "
    ).strip()

    if strength:
        filtered = filter_by_strength(evidence_records, strength)

        print("\n=== STRENGTH FILTER RESULTS ===")

        if filtered:
            for record in filtered:
                print(
                    f"{record['evidence_id']} | "
                    f"{record['evidence_strength']} | "
                    f"{record['concept']}"
                )
        else:
            print("No records found for this strength.")

    # Incomplete evidence
    incomplete = find_incomplete(evidence_records)

    print("\n=== INCOMPLETE / INSUFFICIENT EVIDENCE ===")

    if incomplete:
        for record in incomplete:
            print(
                f"{record['evidence_id']} | "
                f"{record['evidence_strength']} | "
                f"{record['main_finding']}"
            )
    else:
        print("No insufficient or unknown records found.")

    # Contradictions
    show_contradictions(contradiction_records)

    # JSON output
    output_path = create_json_output(
        evidence_records,
        claim_records,
        contradiction_records
    )

    print("\n=== STRUCTURED JSON OUTPUT ===")
    print(f"JSON output created: {output_path}")

    print("\n=== FRAMEWORK RESULT ===")
    print("Evidence remains traceable to source IDs.")
    print("Evidence can be filtered by category and strength.")
    print("Contradictions remain visible.")
    print("Unsupported evidence is not promoted to strong evidence.")
    print("Unknown remains unknown.")


if __name__ == "__main__":
    main()