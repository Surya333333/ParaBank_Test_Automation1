import json

class payloads:

    @staticmethod
    def load_test_data(index=0):
        """Loads user data from the JSON file."""
        file_path = r"C:\Users\surya\.vscode\ParaBank_Test_Automation1\Data\test_data.json"
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data["data"][index]

    @staticmethod
    def build_customer_payload(user_data):
        """Builds the customer JSON payload structure used across multiple APIs."""
        payload = {
            "name": user_data["payee_name"],
            "address": {
                "street": user_data["user_address"],
                "city": user_data["user_city"],
                "state": user_data["user_state"],
                "zipCode": user_data["user_zip_code"]
            },
            "phoneNumber": user_data["phoneNumber"],
            "accountNumber": int(user_data["accountNumber"])
        }
        return payload
