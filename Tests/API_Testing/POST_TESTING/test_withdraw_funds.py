
from api_clients.Post_API.withdraw_funds import post_user_withdraw_funds
from Payloads.common_payload import payloads
import pytest
import json

@pytest.mark.smoke
def test_withdraw_funds():
    accountId = 13899
    amount = "122.00"
    user_data = payloads.load_test_data()  # you can also pass an index if you want: load_test_data(0)

    #  Build the payload from the loaded data
    payload = payloads.build_customer_payload(user_data)
    response = post_user_withdraw_funds.POST_withdraw_funds(payload,accountId = accountId ,amount = amount)
    print("Status Code:", response.status_code)
    print("\nResponse Body:", response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
