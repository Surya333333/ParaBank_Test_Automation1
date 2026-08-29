from api_clients.Post_API.update_customer_information import Update_user_Details_class
import pytest
from Payloads.common_payload import payloads


@pytest.mark.smoke
def test_update_customers_details():
    Customer_id = 12767
    firstName = "Sachin Kumar"
    lastName = "Tiwari"
    street = "Janta Bazar"
    city= "Chapra"
    state = "Bihar"
    zipCode = 841224
    phoneNumber = 7903809668
    ssn = 123-45-6789
    username = "Sachin121111@"
    password = "Sachin306@"
    user_data = payloads.load_test_data()
    payload = payloads.build_customer_payload(user_data)
    response = Update_user_Details_class.update_user_details_function(payload,Customer_id = Customer_id,firstName =firstName,lastName =lastName,street = street,city =city,state=state,zipCode = zipCode,phoneNumber =phoneNumber,ssn=ssn,username =username,password =password)
    print("Status Code:", response.status_code)
    print("\nResponse Body:", response.text)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
