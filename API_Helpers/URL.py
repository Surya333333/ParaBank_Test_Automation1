
class URL:
    BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"

    @staticmethod
    def bill_pay_url():
        return f"{URL.BASE_URL}/billpay"

    @staticmethod
    def deposit_url():
        return f"{URL.BASE_URL}/deposit"

    @staticmethod
    def transfer_amount_url():
        return f"{URL.BASE_URL}/transfer"

    @staticmethod
    def account_id(account_number):
        return f"{URL.BASE_URL}/accounts/{account_number}"

    @staticmethod
    def customer_id(customer_number):
        return f"{URL.BASE_URL}/customers/{customer_number}/accounts"

    @staticmethod
    def account_transaction(account_number):
        return f"{URL.BASE_URL}/accounts/{account_number}/transactions"

    @staticmethod
    def create_transaction(bank_account, transaction_amount):
        return f"{URL.BASE_URL}/accounts/{bank_account}/transactions/amount/{transaction_amount}"

    @staticmethod
    #https://parabank.parasoft.com/parabank/services/bank/accounts/36321/transactions/month/october/type/1
    def transaction_by_month_and_account(Account_id,Month_name,Transaction_type):
        return f"{URL.BASE_URL}/accounts/{Account_id}/transactions/month/{Month_name}/type/{Transaction_type}"
    @staticmethod
    def transaction_for_date_range(Account_id,from_date,to_date):
        #https://parabank.parasoft.com/parabank/services/bank/accounts/36321/transactions/fromDate/16-10-2025/toDate/16-10-2025
        return f"{URL.BASE_URL}/accounts/{Account_id}/transactions/fromDate/{from_date}/toDate/{to_date}"
    @staticmethod
    def fetch_transactions(Account_id,onDate):
        #https: // parabank.parasoft.com / parabank / services / bank / accounts / 21003 / transactions / onDate / 17 - 10 - 25
        return f"{URL.BASE_URL}/accounts/{Account_id}/transactions/onDate/{onDate}"
    @staticmethod
    def create_account():
        #https://parabank.parasoft.com/parabank/services/bank/createAccount?customerId=12434&newAccountType=2&fromAccountId=13899
        return f"{URL.BASE_URL}/createAccount"
    @staticmethod
    def transfer_amount():
        #https://parabank.parasoft.com/parabank/services/bank/transfer?fromAccountId=13899&toAccountId=16119&amount=122003.00
        return f"{URL.BASE_URL}/transfer"
    @staticmethod
    def withdraw_funds_url():
        #https://parabank.parasoft.com/parabank/services/bank/withdraw?accountId=13899&amount=122003.00
        return f"{URL.BASE_URL}/withdraw"
    @staticmethod
    def get_customer_accounts_url(Customer_id):
        #https://parabank.parasoft.com/parabank/services/bank/customers/12767/accounts
        return f"{URL.BASE_URL}/customers/{Customer_id}/accounts"
    @staticmethod
    def get_customer_details_by_customer_id_url(Customer_id):
        #https://parabank.parasoft.com/parabank/services/bank/customers/12767
        return f"{URL.BASE_URL}/customers/{Customer_id}"
    @staticmethod
    def update_customer_information_url(Customer_id):
        #'https://parabank.parasoft.com/parabank/services/bank/customers/update/12767?firstName=Sachin%20Kumar&lastName=Tiwari&street=Janta%20Bazar&city=Chapra&state=Bihar&zipCode=841224&phoneNumber=7903809668&ssn=123-45-6789&username=Sachin121111%40&password=Sachin306%40
        return f"{URL.BASE_URL}/customers/update/{Customer_id}"
    @staticmethod
    def request_loan():
        #https://parabank.parasoft.com/parabank/services/bank/requestLoan?customerId=12767&amount=122&downPayment=2&fromAccountId=14232
        return f"{URL.BASE_URL}/requestLoan/"
    @staticmethod
    def _put_method_not_allowed_url():
        #https://parabank.parasoft.com/parabank/transfer.htm
        return f"{URL.BASE_URL}"