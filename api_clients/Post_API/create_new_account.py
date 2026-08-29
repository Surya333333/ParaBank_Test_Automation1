from API_Helpers.headers import Headers
from API_Helpers.params import Params
from API_Helpers.response import RequestHandler
from API_Helpers.URL import URL


class Create_Account:
    @staticmethod
    def CREATE_ACCOUNT(payload,customerId,newAccountType,fromAccountId):
        url = URL.create_account()
        params = Params.create_account_params(customerId,newAccountType,fromAccountId)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_post_request(url, params, headers_call, payload)
        return response