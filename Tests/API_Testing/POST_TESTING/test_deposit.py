from Payloads.common_payload import payloads
from api_clients.Post_API.deposit import DEPOSIT
from jsonschema import validate
import json
import pytest

@pytest.mark.smoke
def test_bill_pay():
    account_id = 13899
    amount = 122
    user_data = payloads.load_test_data()
    payload = payloads.build_customer_payload(user_data)
    response = DEPOSIT.bill_pay_response(payload, account_id=account_id, amount=amount)
    #response = post_deposit(payload, account_id=17673, amount=1000)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    assert "Successfully deposited" in response.text
    assert str(amount) in response.text
    assert str(account_id) in response.text
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


    # API return here single string so there is no need for json Schemas


