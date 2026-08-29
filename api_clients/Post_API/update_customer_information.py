from API_Helpers.URL import URL
from API_Helpers.response import RequestHandler
from API_Helpers.params import Params
from API_Helpers.headers import Headers



class Update_user_Details_class:
    @staticmethod
    def update_user_details_function(payload,Customer_id,firstName,lastName,street,city,state,zipCode,phoneNumber,ssn,username,password):
        url = URL.update_customer_information_url(Customer_id)
        params = Params.update_customer_details_param(firstName,lastName,street,city,state,zipCode,phoneNumber,ssn,username,password)
        header_call = Headers.get_headers()
        response = RequestHandler.send_post_request(url,params,header_call,payload)
        return response


    #why we call everything in response body