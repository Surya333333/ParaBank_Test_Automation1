import json
import pytest
from jsonschema import validate
from api_clients.GET_API.transaction_for_date_range import TRANSACTION_FOR_DATE

def test_Transaction_for_date():
    Account_id = 36321
    from_date = "16-10-2025"
    to_date = "16-10-2025"
    response = TRANSACTION_FOR_DATE.transaction_for_date(Account_id, from_date, to_date)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/transaction_for_date_range.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")
