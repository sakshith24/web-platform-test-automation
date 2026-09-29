# Web Platform Test Automation

A Python-based automated testing framework for validating web applications and REST APIs using **Pytest, Playwright, and Requests**.

The project demonstrates automated **UI testing and API testing**, reusable test utilities, positive and negative test scenarios, and HTML test reporting.

## 🚀 Features

* Automated web UI testing with Playwright
* REST API testing using Python Requests
* Pytest-based test execution
* Reusable API client
* Positive and negative test cases
* JSON response validation
* HTTP status-code validation
* HTML test reports using `pytest-html`
* Centralized test data
* Page Object Model structure for UI automation

## 🛠️ Tech Stack

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| Python            | Programming language               |
| Pytest            | Test framework                     |
| Playwright        | Web UI automation                  |
| Requests          | REST API testing                   |
| pytest-playwright | Playwright integration with Pytest |
| pytest-html       | HTML test reporting                |

## 📁 Project Structure

```text
web-platform-test-automation/
│
├── pages/
│   └── # Page Object Model classes
│
├── tests/
│   └── test_api.py
│       # API test cases
│
├── utils/
│   ├── api_client.py
│   │   # Reusable HTTP API client
│   │
│   └── test_data.py
│       # Centralized test data
│
├── pytest.ini
│   # Pytest configuration
│
├── requirements.txt
│   # Project dependencies
│
├── temp_api_test.py
│   # Temporary API testing script
│
└── README.md
```

## 🧪 Testing Coverage

### API Testing

The API test suite uses the JSONPlaceholder API for testing REST API operations.

Current test scenarios include:

* **GET** — Retrieve a post
* **POST** — Create a new post
* **PUT** — Update an existing post
* **DELETE** — Delete a post
* **Negative testing** — Verify behavior for a non-existent resource

The tests validate:

* HTTP status codes
* Response content type
* JSON response structure
* Required response fields
* Returned values against the request payload
* Error responses

For example, the GET test verifies that the response contains fields such as `userId`, `id`, `title`, and `body`.

## 🔌 Reusable API Client

The project contains a reusable `APIClient` class instead of writing HTTP requests directly inside every test.

```python
class APIClient:
    def get(self, endpoint, params=None, headers=None):
        ...

    def post(self, endpoint, data=None, json=None, headers=None):
        ...

    def put(self, endpoint, data=None, json=None, headers=None):
        ...

    def delete(self, endpoint, headers=None):
        ...
```

The client receives a base URL and builds the complete endpoint URL automatically. This makes the API tests easier to maintain and reuse.

## 🌐 UI Test Automation

The project also includes a `pages/` structure for organizing browser automation using the **Page Object Model (POM)**.

The Page Object approach separates:

```text
Test Logic
    ↓
Page Objects
    ↓
Browser Interaction
```

This helps keep test cases readable and makes UI locators and browser interactions easier to maintain.

## 📊 Test Data

Common test data is centralized inside:

```text
utils/test_data.py
```

The repository includes test configuration for:

* API base URL
* UI base URL
* Demo login credentials
* Product information
* Checkout information

For example, the current test data contains the SauceDemo URL and standard demo credentials.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sakshith24/web-platform-test-automation.git
```

### 2. Navigate into the project

```bash
cd web-platform-test-automation
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

The project requirements include Pytest, Requests, Playwright, pytest-playwright, and pytest-html.

### 6. Install Playwright browsers

```bash
playwright install
```

## ▶️ Running Tests

Run the complete test suite:

```bash
pytest
```

Run API tests:

```bash
pytest tests/test_api.py
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests and generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

## 📈 Test Reporting

The project uses `pytest-html` to generate an HTML test report.

```bash
pytest --html=report.html --self-contained-html
```

After execution, open:

```text
report.html
```

The report provides an overview of:

* Passed tests
* Failed tests
* Skipped tests
* Test execution details
* Test duration
* Environment information

## 🧩 Pytest Configuration

The project uses `pytest.ini` for test configuration.

The configuration specifies:

* Minimum Pytest version
* Test discovery directory
* Strict marker handling
* Console logging

Tests are discovered from the `tests` directory.

## 🔍 Example API Test

```python
def test_get_post(api_client):
    response = api_client.get('/posts/1')

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data
```

This demonstrates the basic testing flow:

```text
Send API Request
       ↓
Receive Response
       ↓
Check Status Code
       ↓
Parse JSON
       ↓
Validate Response
       ↓
Pass / Fail
```

## 🧪 Testing Strategy

The project follows a combination of:

### Positive Testing

Verifies that valid operations work correctly.

Examples:

* Successfully retrieving a post
* Successfully creating a post
* Successfully updating a post
* Successfully deleting a post

### Negative Testing

Verifies that the application handles invalid scenarios correctly.

Example:

```text
Request non-existent post
        ↓
Expected HTTP 404
        ↓
Validate error response
```

## 🎯 Project Objectives

The main objectives of this project are to demonstrate:

* Automated software testing
* API testing
* Browser automation
* Test case design
* Test data management
* Reusable automation utilities
* Pytest fixtures
* Response validation
* Negative testing
* Automated test reporting

## 🔮 Future Improvements

Possible improvements for the framework include:

* Add more UI test scenarios
* Add authentication testing
* Add API schema validation
* Add parameterized test cases
* Add environment-based configuration
* Add screenshots for failed UI tests
* Add parallel test execution
* Add GitHub Actions CI/CD
* Add structured logging
* Add test tags such as `smoke`, `regression`, and `api`
* Add integration between API and UI test flows

## 📄 License

This project is intended for learning and demonstration of automated software testing concepts.
