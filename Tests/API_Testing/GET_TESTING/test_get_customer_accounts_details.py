import json
import pytest
from api_clients.GET_API.get_customer_accounts_details import get_account_details
from jsonschema import validate

@pytest.mark.smoke
def test_customer_account_details():
    Customer_id = 12767

    response = get_account_details.user_account_details(Customer_id = Customer_id)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/get_customer_account_details.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")


