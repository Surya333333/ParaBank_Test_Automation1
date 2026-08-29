import json
import pytest
from jsonschema import validate
from api_clients.Post_API.create_new_account import Create_Account
from Payloads.common_payload import payloads


@pytest.mark.smoke
def test_create_new_account():
    customerId = "12434"
    newAccountType = "2"
    fromAccountId = "13899"
    user_data = payloads.load_test_data()
    payload = payloads.build_customer_payload(user_data)

    response = Create_Account.CREATE_ACCOUNT(customerId =customerId, newAccountType= newAccountType, fromAccountId =fromAccountId,payload = payload)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/create_account_response.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")
