from API_Helpers.URL import URL
from API_Helpers.response import RequestHandler
from API_Helpers.headers import Headers


class customerID:
    @staticmethod
    def customer_id(customer_number, payload=None):
        url = URL.customer_id(customer_number)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_get_request(url, headers_call, payload=payload)
        return response
