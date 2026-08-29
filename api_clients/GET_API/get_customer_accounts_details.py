from API_Helpers.URL import URL
from API_Helpers.response import RequestHandler
from API_Helpers.headers import Headers

class get_account_details:
    @staticmethod
    def user_account_details(Customer_id,payload = None):
        url = URL.get_customer_accounts_url(Customer_id)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_get_request(url, headers_call, payload=payload)
        return response
    