class Locators:
    register = "//a[text()='Register']"
    first_name = "//input[@id='customer.firstName']"
    last_name = "//input[@id='customer.lastName']"
    address = "//input[@id='customer.address.street']"
    city = "//input[@id='customer.address.city']"
    state = "//input[@id='customer.address.state']"
    zip_code = "//input[@id='customer.address.zipCode']"
    phone_number = "//input[@id='customer.phoneNumber']"
    ssn_number = "//input[@id='customer.ssn']"
    user_name_id = "//input[@id='customer.username']"
    password = "//input[@id='customer.password']"
    confirm_password = "//input[@id='repeatedPassword']"
    register_button = "//input[contains(@value,'Register')]"

    #Welcome_note
    Welcome_note = "//div[@id='rightPanel']"

    #login Page
    login_username = "//input[@name='username']"
    login_password = "//input[@name='password']"
    login_submit = "//input[@value='Log In']"

    #login with Wrong user error
    error_note ="//div[@id='rightPanel']"
    # when try to Login with existing user
    existing_user_error = "//span[@id='customer.username.errors']"

    #open saving account
    saving_account ="//a[@href='openaccount.htm']"
    select_saving = "//select[@id='type']"
    option_2 = "//option[contains(text(),'SAVINGS')]"
    create_account = "//input[contains(@value,'Open New Account')]"
    money_selection = "//select[contains(@id,'fromAccountId')]"
    successfuly_checking_creation ="//div[@id='openAccountResult']//h1"
    select_amount ="//select[@id='fromAccountId']"

    #forgot account
    forgot = "//a[contains(text(),'Forgot login info?')]"
    forgot_button = "//input[contains(@value,'Find My Login Info')]"
    first_name_1 ="//input[@id='firstName']"
    last_name_1 = "//input[@id='lastName']"
    forgot_address = "//input[@id='address.street']"
    forgot_city = "//input[@id='address.city']"
    forgot_state = "//input[@id='address.state']"
    forgot_zip_code = "//input[@id='address.zipCode']"
    forgot_ssn = "//input[@id='ssn']"
    Right_panel = "//div[@id='rightPanel']"
    account_message ="//h1[contains(text(),'Account Opened!')]"
    account_message_1 ="//p[contains(text(),'Congratulations, your account is now open.')]"
    account_message_2 = "//b[contains(text(),'Your new account number:')]"

    Account_opened = "//div[contains(@id,'openAccountResult')]"
    # Account overview

    overview = "//a[contains(text(),'Accounts Overview')]"
    tittle_compare= "(//div[@id='showOverview'])[1]"

    #Transfer bill
    click_on_transfer = "//a[@href ='transfer.htm']"
    transfer_funds ="//input[@id ='amount']"
    from_bank = "//select[@id ='fromAccountId']"
    to_bank = "//select[@id ='toAccountId']"
    transfer_money_button = "//input[@type ='submit']"
    transfer_completion_message ="//div[@id ='showResult']"

    #bill pay
    bill_pay_click = "//a[contains(text(),'Bill Pay')]"
    payee = "//input[contains(@name,'payee.name')]"
    payee_number = "//input[contains(@name,'payee.phoneNumber')]"
    payee_account = "//input[contains(@name,'payee.accountNumber')]"
    payee_confirm_account = "//input[contains(@name,'verifyAccount')]"
    amount = "//input[contains(@name,'amount')]"
    select_account = "//select[contains(@name,'fromAccountId')]"
    send_money = "//input[contains(@value,'Send Payment')]"
    payee_address = "//input[@name ='payee.address.street']"
    payee_city = "//input[@name ='payee.address.city']"
    payee_state = "//input[@name ='payee.address.state']"
    payee_zipcode ="//input[@name ='payee.address.zipCode']"
    bill_payment_message = "//div[@id='billpayResult']"

    # Contact_us
    contact = "//a[@href='contact.htm']"
    contact_name ="//input[@id='name']"
    contact_email = "//input[@id='email']"
    contact_phone ="//input[@id='phone']"
    contact_message = "//textarea[@id='message']"
    contact_send_button = "//input[@type='submit']"
    welcome_note ="//div[@id='rightPanel']"

    #Request Loan
    click_on_loan_request = "//a[@href='requestloan.htm']"
    loan_amount="//input[@id='amount']"
    down_payment = "//input[@id='downPayment']"
    select_account_loan = "//select[@id='fromAccountId']"
    loan_apply = "//input[@value='Apply Now']"
    #request_loan = "//div[@id='requestLoanResult']"
    loan_req = "//div[@id='requestLoanResult']//h1"
    loan_provider = "(//tr)[5]"
    loan_date ="(//tr)[6]"
    loan_status = "(//tr)[7]"
    loan_error = "//div[@id='loanRequestDenied']"
    # about us page
    about_us = "//div[@id='rightPanel']"
    click_on = "//li[@class='aboutus']"

    #Logout
    logout_button = "//a[contains(text(),'Log Out')]"

    #Account overview
    user_accounts = "//div[@id ='showOverview']"




