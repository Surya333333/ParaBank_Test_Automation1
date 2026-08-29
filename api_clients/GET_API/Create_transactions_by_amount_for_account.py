from API_Helpers.URL import URL
from API_Helpers.response import RequestHandler
from API_Helpers.headers import Headers

class CREATE_TRANSACTIONS:
    @staticmethod
    def create_transactions(bank_accounts,transaction_amount,payload = None):
        url = URL.create_transaction(bank_accounts,transaction_amount)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_get_request(url, headers_call, payload= payload)
        return response