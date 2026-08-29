Test Strategy – ParaBank

## 1. Introduction
Define the overall testing approach, tools, and responsibilities for ParaBank automation testing.
Testing includes both Web UI and REST API layers.

---

## 2. Scope
*In Scope:*
- Web UI functional testing (Selenium + Pytest)
- API testing (Requests library)
- Regression, Smoke, and Sanity testing

*Out of Scope:*
- Load & Performance testing
- Security testing

---

## 3. Test Levels
- Unit Testing  
- Integration Testing  
- System Testing  
- Regression Testing  
- UAT

---

## 4. Testing Types
| Type | Description |
|------|--------------|
| Functional | Validate UI and API features |
| Smoke | Verify key functionalities post-build |
| Regression | Validate stability after fixes |
| UI Automation | Selenium with POM |
| API Validation | Requests with JSON schema |

---

## 5. Tools & Frameworks
| Category | Tools |
|-----------|--------|
| Test Management | Jira + Confluence |
| Automation | Selenium, Pytest, Requests |
| Reporting | Allure / HTML Reports |
| CI/CD | Jenkins |
| Source Control | GitHub |

---

## 6. Test Environment
| Environment | URL | Notes |
|--------------|-----|-------|
| QA | https://parabank.parasoft.com/parabank/index.htm | Main test environment |

---

## 7. Roles & Responsibilities
| Role | Responsibility |
|------|----------------|
| QA Engineer | Test case design & execution |
| Automation Engineer | Script maintenance |
| Test Lead | Planning, reporting, review |
| Developer | Fix defects |

---

## 8. Reporting
- Automated execution via Jenkins  
- Daily summary in Confluence  
- Weekly report shared with stakeholders