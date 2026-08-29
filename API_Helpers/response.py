import requests
import allure
import json


class RequestHandler:

    @staticmethod
    def send_post_request(url, params, headers, payload):
        with allure.step(f"POST request to {url}"):
            allure.attach(str(headers), name="Request Headers", attachment_type=allure.attachment_type.TEXT)
            allure.attach(json.dumps(payload, indent=2, default=str), name="Request Payload", attachment_type=allure.attachment_type.JSON)

            response = requests.post(url, params=params, json=payload, headers=headers)

            allure.attach(str(response.status_code), name="Response Status Code", attachment_type=allure.attachment_type.TEXT)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)

        return response

    @staticmethod
    def send_get_request(url, headers, params=None, payload=None):
        with allure.step(f"GET request to {url}"):
            allure.attach(str(headers), name="Request Headers", attachment_type=allure.attachment_type.TEXT)
            if params:
                allure.attach(json.dumps(params, indent=2, default=str), name="Request Params", attachment_type=allure.attachment_type.JSON)

            response = requests.get(url, headers=headers, params=params, json=payload)

            allure.attach(str(response.status_code), name="Response Status Code", attachment_type=allure.attachment_type.TEXT)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)

        return response

    @staticmethod
    def send_put_request(url, headers, params=None, payload=None):
        with allure.step(f"PUT request to {url}"):
            allure.attach(str(headers), name="Request Headers", attachment_type=allure.attachment_type.TEXT)
            allure.attach(json.dumps(payload, indent=2, default=str), name="Request Payload", attachment_type=allure.attachment_type.JSON)

            response = requests.put(url, headers=headers, params=params, json=payload)

            allure.attach(str(response.status_code), name="Response Status Code", attachment_type=allure.attachment_type.TEXT)
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.JSON)

        return response
