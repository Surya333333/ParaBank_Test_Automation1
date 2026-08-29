from API_Helpers.URL import URL
from API_Helpers.headers import Headers
from API_Helpers.response import RequestHandler

class TRANSACTION_BY_M_AND_A:
    @staticmethod
    def month_account(Account_id,Month_name,Transaction_type,payload = None ):
        url = URL.transaction_by_month_and_account(Account_id,Month_name,Transaction_type)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_get_request(url, headers_call, payload= payload)
        return response
