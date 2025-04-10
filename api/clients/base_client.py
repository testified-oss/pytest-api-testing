import requests


class BaseAPIClient:
    """
    Base API client for making HTTP requests.
    This client provides a foundation for creating API-specific clients.
    """
    
    def __init__(self, base_url, timeout=10, auth=None):
        """
        Initialize the API client.
        
        Args:
            base_url (str): The base URL for the API
            timeout (int): Request timeout in seconds
            auth (tuple): Basic auth tuple (username, password)
        """
        self.base_url = base_url
        self.timeout = timeout
        self.auth = auth
        self.session = requests.Session()
        
        # Set up session with auth if provided
        if auth:
            self.session.auth = auth
    
    def get(self, endpoint, params=None, **kwargs):
        """
        Make a GET request to the API.
        
        Args:
            endpoint (str): The API endpoint to call
            params (dict): Query parameters
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response: The HTTP response object
        """
        kwargs.setdefault('timeout', self.timeout)
        return self.session.get(f"{self.base_url}{endpoint}", params=params, **kwargs)
    
    def post(self, endpoint, data=None, json=None, **kwargs):
        """
        Make a POST request to the API.
        
        Args:
            endpoint (str): The API endpoint to call
            data (dict): Form data to send
            json (dict): JSON data to send
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response: The HTTP response object
        """
        kwargs.setdefault('timeout', self.timeout)
        return self.session.post(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)
    
    def put(self, endpoint, data=None, json=None, **kwargs):
        """
        Make a PUT request to the API.
        
        Args:
            endpoint (str): The API endpoint to call
            data (dict): Form data to send
            json (dict): JSON data to send
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response: The HTTP response object
        """
        kwargs.setdefault('timeout', self.timeout)
        return self.session.put(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        """
        Make a DELETE request to the API.
        
        Args:
            endpoint (str): The API endpoint to call
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response: The HTTP response object
        """
        kwargs.setdefault('timeout', self.timeout)
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)
    
    def patch(self, endpoint, data=None, json=None, **kwargs):
        """
        Make a PATCH request to the API.
        
        Args:
            endpoint (str): The API endpoint to call
            data (dict): Form data to send
            json (dict): JSON data to send
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response: The HTTP response object
        """
        kwargs.setdefault('timeout', self.timeout)
        return self.session.patch(f"{self.base_url}{endpoint}", data=data, json=json, **kwargs)
    
    def close(self):
        """
        Close the session.
        """
        self.session.close() 