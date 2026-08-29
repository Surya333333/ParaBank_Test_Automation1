# Automation Framework Documentation – ParaBank

## Overview
Automation framework developed using Python, Selenium, Pytest, and Requests.

## Structure
ParaBank_Test_Automation/
│
├── api_clients/
│ └── # Handles all API request methods (GET, POST, PUT, DELETE)
│
├── Page_Pom/
│ └── # Page Object Model (POM) structure for UI automation
│
├── Data/
│ └── # Contains test data in JSON format
│
├── Tests/
│ └── # Holds all test cases (UI + API)
│
├── Reports/
│ └── # Stores Allure and HTML test reports
│
└── Config/
└── # Contains environment configuration and credentials



---

## ⚙️ Tools & Technologies
- **Language:** Python  
- **Frameworks:** Pytest, Selenium, Requests  
- **Reporting:** Allure, pytest-html  
- **Design Pattern:** Page Object Model (POM)  
- **Version Control:** Git / GitHub  

---

## 🚀 Execution Commands

### Run all tests
```bash
pytest -v
