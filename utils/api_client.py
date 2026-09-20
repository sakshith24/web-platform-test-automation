import requests

class APIClient:
    def __init__(self, base_url):
        """
        Initializes the APIClient with a base URL.
        """
        self.base_url = base_url

    def _get_url(self, endpoint):
        """
        Constructs the full URL for a given endpoint.
        """
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint, params=None, headers=None):
        """
        Sends a GET request to the specified endpoint.
        """
        url = self._get_url(endpoint)
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        """
        Sends a POST request to the specified endpoint with data or JSON payload.
        """
        url = self._get_url(endpoint)
        response = requests.post(url, data=data, json=json, headers=headers)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        """
        Sends a PUT request to the specified endpoint with data or JSON payload.
        """
        url = self._get_url(endpoint)
        response = requests.put(url, data=data, json=json, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        """
        Sends a DELETE request to the specified endpoint.
        """
        url = self._get_url(endpoint)
        response = requests.delete(url, headers=headers)
        return response
