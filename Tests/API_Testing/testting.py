import requests


response = requests.get("https://parabank.parasoft.com/parabank/services/bank/login/SRajni731%40/Sachin306%40")

print(response.status_code)
print(response.headers)
