import json
from jsonschema import validate
from api_clients.GET_API.Create_transactions_by_amount_for_account import CREATE_TRANSACTIONS

import pytest

@pytest.mark.smoke
def test_accountNumber():
    bank_accounts = 99591
    transaction_amount = 122.00
    response = CREATE_TRANSACTIONS.create_transactions(bank_accounts,transaction_amount)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()
    with open("Schemas/Create_transactions_by_amount_for_account.json") as f:
        schema = json.load(f)
    if response_json:
        validate(instance=response_json, schema=schema)
        print("Transactions JSON is valid")
    else:
        print(" Empty list — no transactions found, skipping schema validation.")