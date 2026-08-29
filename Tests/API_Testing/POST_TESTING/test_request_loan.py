from api_clients.Post_API.request_loan import REQUEST_LOAN
import pytest
import json
from Payloads.common_payload import payloads
from jsonschema import validate

@pytest.mark.smoke
def test_request_loan():

    customerId = 12767,
    amount = 122,
    downPayment = 2,
    fromAccountId = 14232
    user_data = payloads.load_test_data()  # you can also pass an index if you want: load_test_data(0)

    #  Build the payload from the loaded data
    payload = payloads.build_customer_payload(user_data)

    #  Call API Client function
    response = REQUEST_LOAN.request_loan_by_user(payload,customerId = customerId,amount=amount,downPayment =downPayment, fromAccountId=fromAccountId)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    response_json = response.json()

    # Load schema
    with open("Schemas/request_loan.json") as f:
        schema = json.load(f)

    # Validate against schema (only if non-empty)
    if response_json:
        validate(instance=response_json, schema=schema)
    else:
        print("⚠️ Empty list — no transactions found, skipping schema validation.")
