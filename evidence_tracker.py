import csv
import json

# ---------------------------------------------------------
# BIOSIMILARITY EVIDENCE TRACKER
# ---------------------------------------------------------

FILE_PATH = "sample_data/candidate_evidence.csv"

print("=" * 70)
print("BIOSIMILARITY EVIDENCE TRACKER")
print("=" * 70)

print()
print("IMPORTANT:")
print("This is an evidence-organisation tool, not a regulatory approval system.")
print()


# ---------------------------------------------------------
# 1. LOAD CSV DATASET
# ---------------------------------------------------------

def load_evidence():
    records = []

    with open(FILE_PATH, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


# ---------------------------------------------------------
# 2. SEARCH BY REFERENCE OR CANDIDATE PRODUCT
# ---------------------------------------------------------

def search_product(records, search_term):

    search_term = search_term.lower()

    results = []

    for record in records:

        reference = record["Reference Product"].lower()
        candidate = record["Candidate Product"].lower()

        if search_term in reference or search_term in candidate:
            results.append(record)

    return results


# ---------------------------------------------------------
# 3. FILTER BY EVIDENCE CATEGORY
# ---------------------------------------------------------

def filter_category(records, category):

    category = category.lower()

    return [
        record
        for record in records
        if record["Evidence Category"].lower() == category
    ]


# ---------------------------------------------------------
# 4. FILTER BY VALIDATION STATUS
# ---------------------------------------------------------

def filter_validation(records, status):

    status = status.lower()

    return [
        record
        for record in records
        if record["Validation Status"].lower() == status
    ]


# ---------------------------------------------------------
# 5. DISPLAY EVIDENCE RECORDS
# ---------------------------------------------------------

def display_records(records):

    if not records:
        print("No evidence records found.")
        return

    print()
    print("=" * 70)
    print("EVIDENCE RECORDS")
    print("=" * 70)

    for record in records:

        print()
        print("Evidence ID:", record["Evidence ID"])
        print("Reference Product:", record["Reference Product"])
        print("Candidate Product:", record["Candidate Product"])
        print("Evidence Category:", record["Evidence Category"])
        print("Study/Source:", record["Study/Source"])
        print("Measurement:", record["Measurement"])
        print("Result:", record["Result"])
        print("Control:", record["Control"])
        print("Evidence Quality:", record["Evidence Quality"])
        print("Validation Status:", record["Validation Status"])
        print("Limitation:", record["Limitation"])
        print("Reviewer Note:", record["Reviewer Note"])
        print("-" * 70)


# ---------------------------------------------------------
# 6. DISPLAY LIMITATIONS
# ---------------------------------------------------------

def display_limitations(records):

    print()
    print("=" * 70)
    print("KNOWN LIMITATIONS")
    print("=" * 70)

    if not records:
        print("No records available.")
        return

    for record in records:

        print(
            record["Evidence ID"],
            "->",
            record["Limitation"]
        )


# ---------------------------------------------------------
# 7. IDENTIFY INCOMPLETE EVIDENCE
# ---------------------------------------------------------

def identify_incomplete_evidence(records):

    incomplete = []

    for record in records:

        status = record["Validation Status"].upper()
        quality = record["Evidence Quality"].upper()

        limitation = record["Limitation"].strip()
        reviewer_note = record["Reviewer Note"].strip()

        if (
            status in ["NEEDS REVIEW", "INSUFFICIENT", "PARTIAL"]
            or quality in ["LOW", "INSUFFICIENT"]
            or not limitation
            or not reviewer_note
        ):
            incomplete.append(record)

    return incomplete


# ---------------------------------------------------------
# 8. COMPARE REFERENCE VS CANDIDATE EVIDENCE
# ---------------------------------------------------------

def compare_reference_candidate(records, candidate):

    candidate_records = [
        record
        for record in records
        if record["Candidate Product"].lower() == candidate.lower()
    ]

    categories = {}

    for record in candidate_records:

        category = record["Evidence Category"]

        if category not in categories:
            categories[category] = {
                "records": 0,
                "verified": 0,
                "needs_review": 0,
                "insufficient": 0
            }

        categories[category]["records"] += 1

        status = record["Validation Status"].upper()

        if status == "VERIFIED":
            categories[category]["verified"] += 1

        elif status == "NEEDS REVIEW":
            categories[category]["needs_review"] += 1

        elif status == "INSUFFICIENT":
            categories[category]["insufficient"] += 1

    return categories


# ---------------------------------------------------------
# 9. CREATE STRUCTURED JSON
# ---------------------------------------------------------

def create_json(records):

    incomplete = identify_incomplete_evidence(records)

    candidate_products = sorted(
        set(
            record["Candidate Product"]
            for record in records
        )
    )

    categories = sorted(
        set(
            record["Evidence Category"]
            for record in records
        )
    )

    verified = sum(
        1
        for record in records
        if record["Validation Status"].upper() == "VERIFIED"
    )

    needs_review = sum(
        1
        for record in records
        if record["Validation Status"].upper() == "NEEDS REVIEW"
    )

    insufficient = sum(
        1
        for record in records
        if record["Validation Status"].upper() == "INSUFFICIENT"
    )

    output = {
        "tool": "Biosimilarity Evidence Tracker",
        "purpose": "Evidence organisation and review support",
        "regulatory_approval_system": False,
        "candidate_products": candidate_products,
        "evidence_categories": categories,
        "evidence_records": len(records),
        "verified": verified,
        "needs_review": needs_review,
        "insufficient": insufficient,
        "incomplete_evidence_count": len(incomplete),
        "known_evidence_gaps": [
            record["Evidence Category"]
            for record in incomplete
        ]
    }

    return output


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():

    # Load data
    records = load_evidence()

    print("CSV loaded successfully.")
    print("Total evidence records:", len(records))

    # -----------------------------------------------------
    # Example search
    # -----------------------------------------------------

    candidate = "Candidate-B"

    search_results = search_product(records, candidate)

    print()
    print("=" * 70)
    print("BIOSIMILARITY EVIDENCE REVIEW")
    print("=" * 70)

    print("Candidate:", candidate)

    print("Evidence Categories:")

    categories = sorted(
        set(
            record["Evidence Category"]
            for record in search_results
        )
    )

    for category in categories:
        print("-", category)

    print("Evidence Records:", len(search_results))

    verified = sum(
        1
        for record in search_results
        if record["Validation Status"].upper() == "VERIFIED"
    )

    needs_review = sum(
        1
        for record in search_results
        if record["Validation Status"].upper() == "NEEDS REVIEW"
    )

    insufficient = sum(
        1
        for record in search_results
        if record["Validation Status"].upper() == "INSUFFICIENT"
    )

    print("Verified:", verified)
    print("Needs Review:", needs_review)
    print("Insufficient:", insufficient)

    # Display records
    display_records(search_results)

    # Display limitations
    display_limitations(search_results)

    # Identify incomplete evidence
    incomplete = identify_incomplete_evidence(search_results)

    print()
    print("=" * 70)
    print("INCOMPLETE EVIDENCE")
    print("=" * 70)

    if incomplete:

        for record in incomplete:
            print(
                record["Evidence ID"],
                "-",
                record["Evidence Category"],
                "-",
                record["Validation Status"]
            )

    else:
        print("No incomplete evidence identified.")

    # -----------------------------------------------------
    # Compare reference and candidate
    # -----------------------------------------------------

    print()
    print("=" * 70)
    print("REFERENCE VS CANDIDATE COMPARISON")
    print("=" * 70)

    comparison = compare_reference_candidate(
        records,
        candidate
    )

    for category, data in comparison.items():

        print()
        print("Category:", category)
        print("Records:", data["records"])
        print("Verified:", data["verified"])
        print("Needs Review:", data["needs_review"])
        print("Insufficient:", data["insufficient"])

    # -----------------------------------------------------
    # JSON OUTPUT
    # -----------------------------------------------------

    json_output = create_json(search_results)

    print()
    print("=" * 70)
    print("STRUCTURED JSON OUTPUT")
    print("=" * 70)

    print(
        json.dumps(
            json_output,
            indent=4
        )
    )


# ---------------------------------------------------------
# START PROGRAM
# ---------------------------------------------------------

if __name__ == "__main__":
    main()