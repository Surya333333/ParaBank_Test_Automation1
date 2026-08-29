from API_Helpers.URL import URL
from API_Helpers.response import RequestHandler
from API_Helpers.headers import Headers

class AccountIDAPI:

    @staticmethod
    def get_account_by_id(account_number):
        url = URL.account_id(account_number)
        headers = Headers.get_headers()
        response = RequestHandler.send_get_request(url, headers)
        return response
