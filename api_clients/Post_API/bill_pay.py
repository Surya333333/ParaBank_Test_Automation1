from API_Helpers.params import Params
from API_Helpers.URL import URL
from API_Helpers.headers import Headers
from API_Helpers.response import RequestHandler

class BILL_PAY:

    @staticmethod
    def bill_pay_response(payload, account_id, amount):
        """Calls the bill pay API"""
        url = URL.bill_pay_url()
        params = Params.bill_pay_params(account_id, amount)
        headers_call = Headers.get_headers()

        # Use the reusable response function
        response = RequestHandler.send_post_request(url, params, headers_call, payload)
        return response
