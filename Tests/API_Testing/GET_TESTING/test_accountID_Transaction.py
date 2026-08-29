from api_clients.GET_API.accountID_Transaction import ACCOUNT_TRANSACTION
from jsonschema import validate
import json
import pytest

def test_transaction():
    account_number = 14454
    response = ACCOUNT_TRANSACTION.accountID_Trans(account_number)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()

    # Load schema
    with open("Schemas/accountID_Transaction.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
        print("Transactions JSON is valid")
    else:
        print(" Empty list — no transactions found, skipping schema validation.")
