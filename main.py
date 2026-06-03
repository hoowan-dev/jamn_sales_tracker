import os
from datetime import datetime, timezone
from dotenv import load_dotenv

# service wrappers
from services.squarespace_service import SquarespaceClient
from services.square_service import SquareClient
from services.google_sheets_service import GoogleSheetsClient

def fetch_and_log_sales():
    print("Initializing clients...")
    
    # 1. Initialize Clients (Pseudocode for now)
    ss_client = SquarespaceClient(api_key=os.getenv('SQUARESPACE_KEY'))
    sq_client = SquareClient(access_token=os.getenv('SQUARE_TOKEN'))
    gs_client = GoogleSheetsClient(credentials_path=os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))

    # For Squarespace, fetch orders since the last sync date
    print("Fetching sales data from Squarespace...")
    current_time_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ss_orders = ss_client.get_orders(modified_after='2023-10-01T00:00:00Z', modified_before=current_time_iso)
    
    # For Square, use the SearchOrders endpoint
    print("Fetching sales data from Square...")
    location_id = os.getenv('SQUARE_LOCATION_ID')
    sq_orders = sq_client.search_orders(location_ids=[location_id]) if location_id else []

    all_sales = []
    
    print(f"Normalizing {len(ss_orders)} Squarespace orders...")
    for order in ss_orders:
        all_sales.append([
            order['createdOn'], 
            order['grandTotal']['value'], 
            'Squarespace', 
            order['orderNumber']
        ])

    print(f"Normalizing {len(sq_orders)} Square orders...")
    for order in sq_orders:
        # In the latest SDK, order data is accessed via attributes
        amount = float(order.total_money.amount or 0) / 100 if order.total_money else 0.0
        all_sales.append([
            order.created_at,
            f"{amount:.2f}",
            'Square',
            order.id
        ])

    if not all_sales:
        print("No new sales found. Google sheet was unaffected.")
        return

    print(f"Appending {len(all_sales)} sales to Google Sheets...")
    all_sales.append([datetime.now().strftime("%Y-%m-%d"), "0.00", "Test Source", "TEST-ID"])
    
    gs_client.append_rows(spreadsheet_id=os.getenv('GOOGLE_SHEET_ID'), rows=all_sales)
    print(f"Successfully logged {len(all_sales)} sales.")

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    
    print("JAMN Sales Tracker Initialized.")
    fetch_and_log_sales()