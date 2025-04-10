import pytest
import os
import json
from api.clients.base_client import BaseAPIClient

# Config fixture for environment management
@pytest.fixture
def config():
    """
    Load configuration based on the environment.
    Default to 'dev' if not specified.
    """
    env = os.environ.get("TEST_ENV", "dev")
    config_dir = os.path.join(os.path.dirname(__file__), "config")
    
    # Config file path
    config_file = os.path.join(config_dir, f"{env}.json")
    
    # Verify config file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file not found: {config_file}")
    
    # Load the configuration
    with open(config_file, "r") as f:
        return json.load(f)

# Base API client fixture using environment configuration
@pytest.fixture
def api_client(config):
    """
    Create a base API client using environment-specific configuration.
    """
    client = BaseAPIClient(
        base_url=config["base_url"],
        timeout=config["timeout"],
        auth=(config["auth"]["username"], config["auth"]["password"]) if "auth" in config else None
    )
    
    # Set default headers if provided in config
    if "headers" in config:
        for key, value in config["headers"].items():
            client.session.headers[key] = value
    
    yield client
    
    # Clean up
    client.close()

# Test data fixture
@pytest.fixture
def test_data(config):
    """
    Provide test data from configuration.
    """
    if "test_data" in config:
        return config["test_data"]
    
    # Default test data if not in config
    return {
        "post_id": 1,
        "user_id": 1
    }

# Endpoints fixture
@pytest.fixture
def endpoints(config):
    """
    Provide API endpoints from configuration.
    """
    if "endpoints" in config:
        return config["endpoints"]
    
    # Default endpoints if not in config
    return {
        "posts": "/posts",
        "users": "/users",
        "comments": "/comments"
    } 