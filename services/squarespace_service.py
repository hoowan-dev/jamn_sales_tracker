import requests

class SquarespaceClient:
    """
    A client to interact with the Squarespace Commerce API.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        # API documentation: https://developers.squarespace.com/commerce-api/orders-introduction
        self.base_url = "https://api.squarespace.com/1.0/commerce/orders"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": "JAMN-Sales-Tracker/1.0"
        }

    def get_orders(self, modified_after=None):
        """
        Fetches orders from Squarespace.
        
        :param modified_after: ISO 8601 formatted string (e.g., '2023-10-01T00:00:00Z')
        """
        params = {}
        if modified_after:
            params['modifiedAfter'] = modified_after
            
        response = requests.get(self.base_url, headers=self.headers, params=params)
        
        if response.status_code == 200:
            return response.json().get('result', [])
        else:
            response.raise_for_status()