.PHONY: setup test test-html test-allure serve-allure clean test-dev test-prod test-env-config

# Default Python command
PYTHON = python3
# Default pytest command with common options
PYTEST = pytest

# Create virtual environment and install dependencies
setup:
	$(PYTHON) -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Run all tests
test:
	$(PYTEST)

# Run tests with HTML reporting
test-html:
	$(PYTEST) --html-report=./report

# Run tests with Allure reporting
test-allure:
	$(PYTEST) --alluredir=./allure-results

# Serve Allure report
serve-allure:
	allure serve allure-results

# Run tests in development environment
test-dev:
	TEST_ENV=dev $(PYTEST)

# Run tests in production environment
test-prod:
	TEST_ENV=prod $(PYTEST)

# Run environment configuration tests
test-env-config:
	TEST_ENV=dev $(PYTEST) tests/test_environment_config.py -v

# Compare environment configurations (run both dev and prod tests)
test-compare-envs:
	@echo "Running tests in development environment..."
	TEST_ENV=dev $(PYTEST) tests/test_environment_config.py -v
	@echo "\nRunning tests in production environment..."
	TEST_ENV=prod $(PYTEST) tests/test_environment_config.py -v

# Clean up generated files
clean:
	rm -rf .pytest_cache
	rm -rf report
	rm -rf allure-results
	rm -rf __pycache__
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete

# Help command
help:
	@echo "Available commands:"
	@echo "  make setup      - Create a virtual environment and install dependencies"
	@echo "  make test       - Run all tests"
	@echo "  make test-html  - Run tests with HTML reporting"
	@echo "  make test-allure - Run tests with Allure reporting"
	@echo "  make serve-allure - Serve the Allure report"
	@echo "  make test-dev   - Run tests in development environment"
	@echo "  make test-prod  - Run tests in production environment"
	@echo "  make test-env-config - Run environment configuration tests"
	@echo "  make test-compare-envs - Compare development and production environments"
	@echo "  make clean      - Clean up generated files"
