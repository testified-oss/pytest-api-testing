import json
import jsonschema


def validate_status_code(response, expected_status):
    """
    Validate response status code.
    
    Args:
        response: The HTTP response object
        expected_status: Expected status code or list of status codes
        
    Returns:
        bool: True if validation passes
        
    Raises:
        AssertionError: If validation fails
    """
    if isinstance(expected_status, list):
        assert response.status_code in expected_status, \
            f"Expected status code {expected_status}, got {response.status_code}"
    else:
        assert response.status_code == expected_status, \
            f"Expected status code {expected_status}, got {response.status_code}"
    return True


def validate_json_response(response):
    """
    Validate that the response contains valid JSON.
    
    Args:
        response: The HTTP response object
        
    Returns:
        dict: Parsed JSON response
        
    Raises:
        AssertionError: If validation fails
    """
    try:
        json_data = response.json()
        return json_data
    except json.JSONDecodeError as e:
        assert False, f"Invalid JSON response: {str(e)}"


def validate_json_schema(data, schema):
    """
    Validate JSON data against a schema.
    
    Args:
        data: JSON data to validate
        schema: JSON schema to validate against
        
    Returns:
        bool: True if validation passes
        
    Raises:
        AssertionError: If validation fails
    """
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        assert False, f"JSON schema validation failed: {str(e)}"


def validate_response_time(response, max_time_ms):
    """
    Validate that the response time is within acceptable limits.
    
    Args:
        response: The HTTP response object
        max_time_ms: Maximum acceptable response time in milliseconds
        
    Returns:
        bool: True if validation passes
        
    Raises:
        AssertionError: If validation fails
    """
    response_time_ms = response.elapsed.total_seconds() * 1000
    assert response_time_ms <= max_time_ms, \
        f"Response time {response_time_ms}ms exceeded maximum {max_time_ms}ms"
    return True


def validate_headers(response, expected_headers):
    """
    Validate that the response contains expected headers.
    
    Args:
        response: The HTTP response object
        expected_headers: Dictionary of expected headers
        
    Returns:
        bool: True if validation passes
        
    Raises:
        AssertionError: If validation fails
    """
    for header, value in expected_headers.items():
        assert header in response.headers, f"Expected header {header} not found"
        if value is not None:
            assert response.headers[header] == value, \
                f"Expected header {header} to be {value}, got {response.headers[header]}"
    return True


def validate_content_type(response, content_type):
    """
    Validate the response content type.
    
    Args:
        response: The HTTP response object
        content_type: Expected content type
        
    Returns:
        bool: True if validation passes
        
    Raises:
        AssertionError: If validation fails
    """
    assert 'Content-Type' in response.headers, "Content-Type header not found"
    assert content_type in response.headers['Content-Type'], \
        f"Expected Content-Type {content_type}, got {response.headers['Content-Type']}"
    return True 