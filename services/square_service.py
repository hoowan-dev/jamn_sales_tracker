import square
from square.environment import SquareEnvironment

class SquareClient:
    """
    A client to interact with the Square API to fetch order data.
    """
    def __init__(self, access_token, environment='production'):
        # The entry point class in the latest SDK is 'Square', not 'Client'
        # The authentication parameter is 'token', and it is keyword-only.
        self.client = square.Square(
            token=access_token,
            environment=SquareEnvironment.SANDBOX if environment.lower() == 'sandbox' else SquareEnvironment.PRODUCTION
        )

    def search_orders(self, location_ids):
        """
        Searches for orders across the specified location IDs.
        """
        try:
            # In the latest SDK, methods take parameters as keyword arguments 
            # and return the result model directly.
            response = self.client.orders.search(location_ids=location_ids)
            return response.orders or []
        except Exception as e:
            print(f"Error fetching Square orders: {e}")
            return []