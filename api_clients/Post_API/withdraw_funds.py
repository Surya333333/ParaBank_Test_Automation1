from API_Helpers.URL import URL
from API_Helpers.response import RequestHandler
from API_Helpers.headers import Headers
from API_Helpers.params import Params

class post_user_withdraw_funds:
    @staticmethod
    def POST_withdraw_funds(payload,accountId,amount):
        url = URL.withdraw_funds_url()

        params = Params.withdraw_funds_params(accountId,amount)
        header_call = Headers.get_headers()
        response = RequestHandler.send_post_request(url, params, header_call, payload)
        return response