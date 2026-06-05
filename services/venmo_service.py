from venmo_api import Client

class VenmoClient:
    """
    A client to interact with the Venmo API to fetch transaction data.
    Note: Venmo does not have an official public API, so this relies on the 
    unofficial `venmo_api` python package (pip install venmo-api).
    """
    def __init__(self, access_token):
        self.client = Client(access_token=access_token)

    def get_transactions(self, limit=50):
        """
        Fetches transactions for the currently authenticated user.
        """
        try:
            my_profile = self.client.user.get_my_profile()
            return self.client.user.get_user_transactions(user_id=my_profile.id, limit=limit)
        except Exception as e:
            print(f"Error fetching Venmo transactions: {e}")
            return []