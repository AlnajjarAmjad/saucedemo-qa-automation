# SauceDemo QA Automation Framework

Automated test suite for the SauceDemo e-commerce demo application, covering UI testing (login, cart, checkout) and API testing, built with Playwright and Python.

## 🛠️ Tech Stack
- **Python** - Programming language
- **Playwright** - Browser automation
- **Pytest** - Test framework
- **Requests** - API testing
- **Page Object Model (POM)** - Design pattern for maintainable test code

## 📁 Project Structure

qa-automation-project/
├── pages/
│ ├── login_page.py
│ ├── inventory_page.py
│ └── checkout_page.py
├── test_login.py
├── test_cart.py
├── test_checkout.py
├── test_api.py
├── conftest.py
├── pytest.ini
└── requirements.txt

## ✅ Test Coverage

**UI Tests:**
- Login (successful, invalid credentials, empty fields)
- Shopping cart (add item, add multiple items, remove item)
- Checkout flow (complete purchase, missing required fields)

**API Tests:**
- GET single user
- POST create user
- PUT update user
- DELETE user
- GET nonexistent user (404 handling)

## 🚀 Setup & Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd qa-automation-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```

3. Create a `.env` file with your API key:

REQREST_API_KEY=your_api_key_here

## ▶️ Running Tests

Run all tests:
```bash
pytest
```

Run with visible browser:
```bash
pytest --headed
```

Run a specific test file:
```bash
pytest test_login.py
```

## 📌 Notes
This project was built as a hands-on learning exercise in test automation, applying Page Object Model design patterns and covering both UI and API testing layers.
