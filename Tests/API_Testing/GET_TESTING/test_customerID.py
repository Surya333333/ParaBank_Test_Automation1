from api_clients.GET_API.customerID import customerID
import json
import pytest
from jsonschema import validate

@pytest.mark.smoke
def test_accountNumber():
    customer_number = 60386
    response = customerID.customer_id(customer_number)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/customerID.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")