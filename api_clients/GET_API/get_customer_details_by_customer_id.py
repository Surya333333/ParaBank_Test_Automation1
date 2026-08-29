from API_Helpers.URL import URL
from API_Helpers.headers import Headers
from API_Helpers.response import RequestHandler

class get_user_details_by_customer_id:
    @staticmethod
    def get_user_details(Customer_id,payload = None):
        url = URL.get_customer_details_by_customer_id_url(Customer_id)
        headers_call = Headers.get_headers()
        response = RequestHandler.send_get_request(url,headers_call,payload = payload)
        return response