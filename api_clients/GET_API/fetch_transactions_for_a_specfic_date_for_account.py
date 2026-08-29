from API_Helpers.URL import URL
from API_Helpers.headers import Headers
from API_Helpers.response import RequestHandler

class FETCH_TRANSACTION:
    @staticmethod
    def fetch_transaction_for_account(Account_id,onDate,payload=None):
        url = URL.fetch_transactions(Account_id,onDate)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_get_request(url, headers_call, payload=payload)
        return response