# Architecture

## Overview

The system is organized into four primary layers:

1. Canonical schema
2. QC engine
3. Synthetic test dataset
4. Automated test and evidence packet

## Flow

```text
Synthetic Evidence Dataset
          |
          v
Canonical Schema
          |
          v
Record Validation
          |
          v
Completeness Check
          |
          +----> Duplicate Detection
          |
          +----> Conflict Detection
          |
          v
Evidence Quality Classification
          |
          v
Human Review Routing
          |
          v
Structured JSON Output