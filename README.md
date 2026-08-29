# 🏦 Parabank Automation Framework

A robust **test automation framework** for the [Parabank Dummy Banking Website](https://parabank.parasoft.com/parabank/index.htm) built with **Python**, **Pytest**, **Selenium**, and **Requests**.  
The framework covers **UI Testing, REST API Testing, Database Validation**, and supports **CI/CD integration**.

---

## 🚀 Features
- ✅ **UI Testing** with Selenium & Page Object Model (POM)  
- ✅ **API Testing** with Python `requests` library & Pytest  
- ✅ **Database Integration** for backend validation (SQL queries)  
- ✅ **Test Data Management** using JSON  
- ✅ **Positive & Negative Test Scenarios**  
- ✅ **Custom HTML/Allure Reports**  
- ✅ **CI/CD ready** (Jenkins/GitHub Actions/GitLab CI)  

---
## 📂 Project Structure

ParaBank_Testing/
│── Data/ # Test data files (JSON, CSV, etc.)
│── Page_Pom/ # Page Object Model classes
│── Reports/ # Test execution reports
│── Tests/ # Test cases
│ ├── Positive_Testing/
│ ├── Negative_Testing/
│ ├── API/ # API test cases
│── api_clients/ # API client utilities
│── capture_screenshot/ # Screenshots on failure
│── conftest.py # Pytest fixtures
│── requirements.txt # Python dependencies
