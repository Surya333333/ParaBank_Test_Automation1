from API_Helpers.URL import URL
from API_Helpers.headers import Headers
from API_Helpers.response import RequestHandler

class TRANSACTION_FOR_DATE:
    @staticmethod
    def transaction_for_date(Account_id,from_date,to_date,payload = None):
        url = URL.transaction_for_date_range(Account_id,from_date,to_date)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_get_request(url, headers_call, payload= payload)
        return response
