from API_Helpers.URL import URL
from API_Helpers.response import RequestHandler
from API_Helpers.params import Params
from API_Helpers.headers import Headers



class TRANSFER_AMOUNT:
    @staticmethod
    def user_transfer_amount(payload,from_account_id,to_account_id,amount):
        url = URL.transfer_amount()
        params = Params.transfer_amount_params(from_account_id,to_account_id,amount)
        header_call = Headers.get_headers()
        response = RequestHandler.send_post_request(url,params,header_call,payload)
        return response