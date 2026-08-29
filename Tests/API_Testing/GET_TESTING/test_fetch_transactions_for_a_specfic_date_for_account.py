from api_clients.GET_API.fetch_transactions_for_a_specfic_date_for_account import FETCH_TRANSACTION
import json
import pytest
from jsonschema import validate

@pytest.mark.smoke
def test_Fetch_transactions_for_a_specfic_date_for_account():
    Account_id = 26997
    onDate = "21-10-25"

    response = FETCH_TRANSACTION.fetch_transaction_for_account(Account_id, onDate)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()

    # Load schema
    with open("Schemas/fetch_transactions_for_a_specfic_date_for_account.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")

