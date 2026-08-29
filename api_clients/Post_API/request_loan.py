from API_Helpers.params import Params
from API_Helpers.URL import URL
from API_Helpers.headers import Headers
from API_Helpers.response import RequestHandler



class REQUEST_LOAN:
    @staticmethod
    def request_loan_by_user(payload,customerId,amount,downPayment,fromAccountId):
        url = URL.request_loan()
        params = Params.request_loan_param(customerId,amount,downPayment,fromAccountId)
        header_call = Headers.get_headers()
        response = RequestHandler.send_post_request(url, params, header_call, payload)
        return response