from api_clients.GET_API.transaction_by_month_and_account import TRANSACTION_BY_M_AND_A
import pytest
import json
from jsonschema import validate


@pytest.mark.smoke
def test_transaction_by_month_and_account():
    Account_id = 36321
    Month_name = "october"
    Transaction_type = 1
    response = TRANSACTION_BY_M_AND_A.month_account(Account_id, Month_name,Transaction_type)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/transaction_by_month_and_account.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")
    print("BUG-101 : API timeout in transfer funds ")
