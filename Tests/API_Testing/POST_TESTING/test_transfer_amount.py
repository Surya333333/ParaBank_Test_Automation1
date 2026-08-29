from Payloads.common_payload import payloads
from api_clients.Post_API.transfer_amount import TRANSFER_AMOUNT
import pytest

@pytest.mark.smoke
def test_post_transfer_amount():
    fromAccount_Id = 13899,
    toAccount_Id = 16119,
    amount = 122003.00
    #  Load data from JSON file (returns dictionary)
    user_data = payloads.load_test_data()  # you can also pass an index if you want: load_test_data(0)

    #  Build the payload from the loaded data
    payload = payloads.build_customer_payload(user_data)

    #  Call API Client function
    response = TRANSFER_AMOUNT.user_transfer_amount(payload,from_account_id=fromAccount_Id,to_account_id=toAccount_Id, amount=amount)


    #  Debug + Assertion
    print("Status Code:", response.status_code)
    print("\nResponse Body:", response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    # Response return in single string so no need of json schema