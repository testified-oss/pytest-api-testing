import pytest
import os
import json
import responses
from utils.validators import (
    validate_status_code,
    validate_json_response,
    validate_content_type
)


class TestEnvironmentConfig:
    """
    Tests that demonstrate environment-specific configurations.
    """
    
    def test_environment_loaded(self, config):
        """Test that the correct environment config is loaded"""
        env = os.environ.get("TEST_ENV", "dev")
        
        # Check base URL matches environment
        if env == "dev":
            assert config["base_url"] == "https://jsonplaceholder.typicode.com"
            assert config["auth"]["username"] == "dev_user"
        elif env == "prod":
            assert config["base_url"] == "https://api.example.com"
            assert config["auth"]["username"] == "prod_user"
        
        # Common assertions
        assert "timeout" in config
        assert "endpoints" in config
        assert "test_data" in config
    
    def test_api_client_configuration(self, api_client, config):
        """Test that the API client is configured correctly"""
        # Check base URL
        assert api_client.base_url == config["base_url"]
        
        # Check timeout
        assert api_client.timeout == config["timeout"]
        
        # Check headers if configured
        if "headers" in config:
            for key, value in config["headers"].items():
                assert api_client.session.headers[key] == value
    
    def test_endpoint_configuration(self, endpoints, config):
        """Test that endpoints are configured correctly"""
        # Verify endpoints match config
        assert endpoints["posts"] == config["endpoints"]["posts"]
        assert endpoints["users"] == config["endpoints"]["users"]
        assert endpoints["comments"] == config["endpoints"]["comments"]
    
    def test_environment_specific_request(self, api_client, endpoints, config):
        """Test a request using environment-specific configuration"""
        env = os.environ.get("TEST_ENV", "dev")
        
        # Print environment info for debugging (will appear in test output)
        print(f"\nRunning in {env} environment")
        print(f"API base URL: {config['base_url']}")
        print(f"Endpoints: {endpoints}")
        
        # Skip actual HTTP request in production environment since api.example.com doesn't exist
        if env == "prod":
            pytest.skip("Skipping actual HTTP request in production environment (api.example.com is fictional)")
        
        # Proceed with the actual request only in development environment
        # Get users endpoint
        response = api_client.get(endpoints["users"])
        
        # Validate response
        validate_status_code(response, 200)
        validate_content_type(response, "application/json")
        
        # Parse and validate response data
        data = validate_json_response(response)
        assert isinstance(data, list), "Expected a list of users"
    
    @pytest.mark.skipif(os.environ.get("TEST_ENV") != "prod", 
                       reason="Test only runs in production environment")
    def test_prod_only_feature(self, api_client, config):
        """Test that only runs in the production environment"""
        assert os.environ.get("TEST_ENV") == "prod"
        assert "X-API-Key" in config["headers"]
        assert config["headers"]["X-API-Key"] == "prod-api-key-12345"
    
    @pytest.mark.skipif(os.environ.get("TEST_ENV") != "dev", 
                       reason="Test only runs in development environment")
    def test_dev_only_feature(self, api_client, config):
        """Test that only runs in the development environment"""
        assert os.environ.get("TEST_ENV") == "dev"
        assert config["retry_attempts"] == 3
        
    @pytest.mark.skipif(os.environ.get("TEST_ENV") != "prod", 
                       reason="Test only runs in production environment")
    @responses.activate
    def test_prod_with_mock(self, api_client, endpoints, config):
        """Test production API with mocked responses"""
        # Set up mock response for users endpoint
        mock_users = [
            {"id": 1, "name": "Production User 1", "email": "user1@example.com"},
            {"id": 2, "name": "Production User 2", "email": "user2@example.com"}
        ]
        
        # Register mock response
        responses.add(
            responses.GET,
            f"{config['base_url']}{endpoints['users']}",
            json=mock_users,
            status=200,
            content_type="application/json"
        )
        
        # Make request to mocked endpoint
        response = api_client.get(endpoints["users"])
        
        # Validate response
        validate_status_code(response, 200)
        validate_content_type(response, "application/json")
        
        # Parse and validate response data
        data = validate_json_response(response)
        assert isinstance(data, list), "Expected a list of users"
        assert len(data) == 2, "Expected 2 users in the mock response"
        assert data[0]["name"] == "Production User 1"
        
        # Verify that the mock was called
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == f"{config['base_url']}{endpoints['users']}" 