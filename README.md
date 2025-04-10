# Pytest API Testing Framework

A comprehensive framework for testing RESTful APIs using pytest and the requests library.

## Features

- Easy test setup and execution
- Modular and reusable components
- Support for both mock and real APIs
- Comprehensive validation of API responses
- Multi-environment support
- HTML and Allure test reports
- CI/CD integration 

## Installation

1. Clone the repository:
```bash
git clone https://github.com/testified-oss/pytest-api-testing.git
cd pytest-api-testing
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Alternatively, you can use the Makefile to set up the environment:
```bash
make setup
```

## Project Structure

```
pytest-api-testing/
├── api/                    # API client layer
│   ├── clients/            # API-specific clients
│   │   ├── __init__.py
│   │   └── base_client.py  # Base API client
│   └── __init__.py
├── config/                 # Configuration files
│   ├── dev.json            # Development environment config
│   └── prod.json           # Production environment config
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_basic_api.py   # Example tests
│   └── test_environment_config.py  # Environment tests
├── utils/                  # Utilities
│   ├── __init__.py
│   └── validators.py       # Response validators
├── conftest.py             # Pytest fixtures
├── Makefile                # Common commands for the project
├── pytest.ini              # Pytest configuration
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```

## Running Tests

Run all tests:
```bash
pytest
# or
make test
```

Run with HTML reporting:
```bash
pytest --html-report=./report
# or
make test-html
```

Run with Allure reporting:
```bash
pytest --alluredir=./allure-results
allure serve allure-results
# or
make test-allure
make serve-allure
```

Run tests for a specific environment:
```bash
TEST_ENV=prod pytest
# or
make test-prod  # for production
make test-dev   # for development
```

Run environment configuration tests:
```bash
make test-env-config
```

Compare development and production environments:
```bash
make test-compare-envs
```

Clean up generated files:
```bash
make clean
```

For a list of all available commands:
```bash
make help
```

## Test Report

The HTML test report will be generated in the `report` directory. Open `report/pytest_html_report.html` in your browser to view it.

## Configuration

You can configure the API endpoints and authentication in the environment-specific config files in the `config` directory:

- `config/dev.json`: Development environment configuration
  - Default base URL: https://jsonplaceholder.typicode.com
  - Development credentials and settings

- `config/prod.json`: Production environment configuration
  - Production API base URL
  - Production credentials and settings
  - Additional headers like API keys

### Configuration Structure

Both configuration files follow the same structure:

```json
{
  "base_url": "https://api.example.com",
  "timeout": 5,
  "retry_attempts": 2,
  "auth": {
    "username": "user",
    "password": "pass"
  },
  "headers": {
    "Content-Type": "application/json",
    "Accept": "application/json"
  },
  "endpoints": {
    "posts": "/api/posts",
    "users": "/api/users",
    "comments": "/api/comments"
  },
  "test_data": {
    "post_id": 1,
    "user_id": 1
  }
}
```

## Adding New Tests

1. Create a new test file in the `tests` directory, following the naming convention `test_*.py`
2. Use the existing fixtures from `conftest.py` or create new ones as needed
3. Import the environment-specific fixtures: `config`, `api_client`, `test_data`, and `endpoints`
4. Write your test cases using the provided utilities
5. Run tests with the desired environment configuration

### Example Test

```python
def test_example(api_client, endpoints, test_data):
    # Get data from environment config
    post_id = test_data["post_id"]
    
    # Use configured endpoints
    response = api_client.get(f"{endpoints['posts']}/{post_id}")
    
    # Validate response
    validate_status_code(response, 200)
    validate_content_type(response, "application/json")
```

### Mocking HTTP Requests

For testing with fictional or unavailable endpoints (especially in production environments), the framework uses the `responses` library to mock HTTP requests:

```python
import responses

# Use the responses decorator to mock HTTP requests
@responses.activate
def test_with_mock(api_client, endpoints, config):
    # Register a mock response
    responses.add(
        responses.GET,
        f"{config['base_url']}{endpoints['users']}",
        json=[{"id": 1, "name": "Test User"}],
        status=200
    )
    
    # Make request - it will be intercepted by the mock
    response = api_client.get(endpoints["users"])
    
    # Test passes without making a real HTTP request
    assert response.status_code == 200
```

This approach allows you to test your code against fictional APIs or avoid making actual API calls during testing.

## License

[MIT License](LICENSE) 

