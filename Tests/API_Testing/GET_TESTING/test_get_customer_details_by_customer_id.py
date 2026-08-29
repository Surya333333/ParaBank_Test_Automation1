

from api_clients.GET_API.get_customer_details_by_customer_id import get_user_details_by_customer_id
import json
import pytest
from jsonschema import validate

@pytest.mark.smoke
def test_get_customer_details_by_customer_id():
    Customer_id = 12767

    response = get_user_details_by_customer_id.get_user_details(Customer_id = Customer_id)
    print("Response Status ",response.status_code)
    print("Response Body:", response.text)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_json = response.json()
    with open("Schemas/get_customer_details_by_customer_id.json") as f:
        schema = json.load(f)
    if response_json:
        validate(instance=response_json, schema=schema)

    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")

