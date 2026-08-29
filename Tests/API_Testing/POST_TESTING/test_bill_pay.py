from Payloads.common_payload import payloads
from api_clients.Post_API.bill_pay import BILL_PAY
import pytest
import json
from jsonschema import validate

@pytest.mark.smoke
def test_bill_pay():
    user_data = payloads.load_test_data()
    payload = payloads.build_customer_payload(user_data)

    response = BILL_PAY.bill_pay_response(payload, account_id=13899, amount=122.00)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/billpay_response_schema.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")