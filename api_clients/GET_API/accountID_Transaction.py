# Get the list of Transaction of account
from API_Helpers.URL import URL
from API_Helpers.response import RequestHandler
from API_Helpers.headers import Headers

class ACCOUNT_TRANSACTION:
    @staticmethod
    def accountID_Trans(account_number,payload = None):
        url = URL.account_transaction(account_number)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_get_request(url, headers_call, payload=payload)
        return response

