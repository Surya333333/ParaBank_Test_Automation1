from api_clients.GET_API.accountID import AccountIDAPI
import json
from jsonschema import validate


def test_account_number():
    account_number = 14454
    response = AccountIDAPI.get_account_by_id(account_number)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()

    # Load schema
    with open("Schemas/accountID.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")
