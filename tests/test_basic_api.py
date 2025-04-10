import pytest
from utils.validators import (
    validate_status_code,
    validate_json_response,
    validate_content_type
)


class TestBasicAPI:
    """
    Basic tests for the API.
    These tests use environment-specific configurations.
    """
    
    def test_get_posts(self, api_client, endpoints):
        """Test GET /posts endpoint"""
        # Send request to the posts endpoint
        response = api_client.get(endpoints["posts"])
        
        # Validate response
        validate_status_code(response, 200)
        validate_content_type(response, "application/json")
        
        # Parse and validate response data
        data = validate_json_response(response)
        assert isinstance(data, list), "Expected a list of posts"
        assert len(data) > 0, "Expected at least one post"
        
        # Validate the structure of the first post
        first_post = data[0]
        assert "id" in first_post, "Post is missing 'id' field"
        assert "userId" in first_post, "Post is missing 'userId' field"
        assert "title" in first_post, "Post is missing 'title' field"
        assert "body" in first_post, "Post is missing 'body' field"
    
    def test_get_post_by_id(self, api_client, endpoints, test_data):
        """Test GET /posts/{id} endpoint"""
        # Get post ID from test data
        post_id = test_data["post_id"]
        
        # Send request
        response = api_client.get(f"{endpoints['posts']}/{post_id}")
        
        # Validate response
        validate_status_code(response, 200)
        validate_content_type(response, "application/json")
        
        # Parse and validate response data
        post = validate_json_response(response)
        assert post["id"] == post_id, f"Expected post with id {post_id}"
        assert "userId" in post, "Post is missing 'userId' field"
        assert "title" in post, "Post is missing 'title' field"
        assert "body" in post, "Post is missing 'body' field"
    
    def test_create_post(self, api_client, endpoints, test_data):
        """Test POST /posts endpoint"""
        # Prepare request data
        post_data = {
            "title": "Test Post",
            "body": "This is a test post created by pytest",
            "userId": test_data["user_id"]
        }
        
        # Send request
        response = api_client.post(endpoints["posts"], json=post_data)
        
        # Validate response
        validate_status_code(response, 201)
        validate_content_type(response, "application/json")
        
        # Parse and validate response data
        created_post = validate_json_response(response)
        assert "id" in created_post, "Created post is missing 'id' field"
        assert created_post["title"] == post_data["title"], "Title doesn't match"
        assert created_post["body"] == post_data["body"], "Body doesn't match"
        assert created_post["userId"] == post_data["userId"], "userId doesn't match"
    
    def test_update_post(self, api_client, endpoints, test_data):
        """Test PUT /posts/{id} endpoint"""
        # Get post ID from test data
        post_id = test_data["post_id"]
        
        # Prepare request data
        updated_data = {
            "title": "Updated Post",
            "body": "This post has been updated by pytest",
            "userId": test_data["user_id"]
        }
        
        # Send request
        response = api_client.put(f"{endpoints['posts']}/{post_id}", json=updated_data)
        
        # Validate response
        validate_status_code(response, 200)
        validate_content_type(response, "application/json")
        
        # Parse and validate response data
        updated_post = validate_json_response(response)
        assert updated_post["id"] == post_id, f"Expected post with id {post_id}"
        assert updated_post["title"] == updated_data["title"], "Title wasn't updated"
        assert updated_post["body"] == updated_data["body"], "Body wasn't updated"
    
    def test_delete_post(self, api_client, endpoints, test_data):
        """Test DELETE /posts/{id} endpoint"""
        # Get post ID from test data
        post_id = test_data["post_id"]
        
        # Send request
        response = api_client.delete(f"{endpoints['posts']}/{post_id}")
        
        # Validate response
        validate_status_code(response, 200)
        
        # For JSONPlaceholder, DELETE typically returns an empty object
        data = validate_json_response(response)
        assert isinstance(data, dict), "Expected an object response"
    
    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_multiple_posts(self, api_client, endpoints, post_id):
        """Test GET /posts/{id} endpoint with multiple post IDs"""
        # Send request
        response = api_client.get(f"{endpoints['posts']}/{post_id}")
        
        # Validate response
        validate_status_code(response, 200)
        validate_content_type(response, "application/json")
        
        # Parse and validate response data
        post = validate_json_response(response)
        assert post["id"] == post_id, f"Expected post with id {post_id}"