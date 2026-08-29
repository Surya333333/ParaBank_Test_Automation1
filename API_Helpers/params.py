class Params:
    @staticmethod
    def bill_pay_params(account_id, amount):
        return {
            "accountId": account_id,
            "amount": amount
        }

    @staticmethod
    def deposit_params(account_id, amount):
        return {
            "accountId": account_id,
            "amount": amount
        }

    @staticmethod
    def transfer_amount_params(from_account_id, to_account_id, amount):
        return {
            "fromAccountId": from_account_id,
            "toAccountId": to_account_id,
            "amount": amount
        }
    @staticmethod
    def create_account_params(customerId,newAccountType,fromAccountId):
        return {
            "customerId":customerId,
            "newAccountType":newAccountType,
            "fromAccountId": fromAccountId
        }
    @staticmethod
    def transfer_account_params(fromAccountId,toAccountId,amount):
        return {
            "fromAccountId" : fromAccountId,
            "toAccountId" : toAccountId,
            "amount" : amount
        }
    @staticmethod
    def withdraw_funds_params(accountId,amount):
        #https://parabank.parasoft.com/parabank/services/bank/withdraw?accountId=13899&amount=122003.00
        return {
            "accountId":accountId,
            "amount":amount
        }
    @staticmethod
    def update_customer_details_param(firstName,lastName,street,city,state,zipCode,phoneNumber,ssn,username,password):
        #'https://parabank.parasoft.com/parabank/services/bank/customers/update/12767?firstName=Sachin%20Kumar&lastName=Tiwari&street=Janta%20Bazar&city=Chapra&state=Bihar&zipCode=841224&phoneNumber=7903809668&ssn=123-45-6789&username=Sachin121111%40&password=Sachin306%40
        return {
            "firstName":firstName,
            "lastName":lastName,
            "street":street,
            "city" :city,
            "state":state,
            "zipCode" :zipCode,
            "phoneNumber":phoneNumber,
            "ssn":ssn,
            "username":username,
            "password":password

        }
    @staticmethod
    def request_loan_param(customerId,amount,downPayment,fromAccountId):
        #https://parabank.parasoft.com/parabank/services/bank/requestLoan?customerId=12767&amount=122&downPayment=2&fromAccountId=14232
        return {
            "customerId":customerId,
            "amount":amount,
            "downPayment":downPayment,
            "fromAccountId":fromAccountId
        }
