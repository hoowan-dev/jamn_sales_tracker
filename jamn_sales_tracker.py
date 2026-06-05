import os
from datetime import datetime, timezone
from dotenv import load_dotenv
import formatting.sheets_formatter as sf

# service wrappers
from services.squarespace_service import SquarespaceClient
from services.square_service import SquareClient
from services.google_sheets_service import GoogleSheetsClient
from services.venmo_service import VenmoClient

def fetch_sales():
    print("Initializing clients...")
    
    # 1. Initialize Clients
    ss_client = SquarespaceClient(api_key=os.getenv('SQUARESPACE_KEY'))
    sq_client = SquareClient(access_token=os.getenv('SQUARE_TOKEN'))
    # vm_client = VenmoClient(access_token=os.getenv('VENMO_ACCESS_TOKEN'))

    all_sales = []

    # For Squarespace, fetch orders since the last sync date
    print("Fetching sales data from Squarespace...")
    current_time_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ss_orders = ss_client.get_orders(modified_after='2023-10-01T00:00:00Z', modified_before=current_time_iso)
    print(f"Normalizing {len(ss_orders)} Squarespace orders...")
    for order in ss_orders:
        for lineItem in order['lineItems']:
            date = sf.formatDate(order['createdOn'], sf.TransactionPlatform.Squarespace)
            transaction_platform = sf.TransactionPlatform.Squarespace
            t_shirt_type = sf.ItemType.fromSquarespace(lineItem['productName'])
            size = sf.Size.fromSquarespace(lineItem['variantOptions'][0]['value'])
            retail_price = float(lineItem['unitPricePaid']['value'])
            earnings = sf.getEarnings(retail_price, sf.TransactionPlatform.Squarespace)
            comments = "Generated from Squarespace API and jamn_sales_tracker"

            entry = sf.generateRowsData(date, transaction_platform, t_shirt_type, size, retail_price, earnings, comments)
            all_sales.append(entry)

    # For Square, use the SearchOrders endpoint
    print("Fetching sales data from Square...")
    location_id = os.getenv('SQUARE_LOCATION_ID')
    sq_orders = sq_client.search_orders(location_ids=[location_id]) if location_id else []
    print(f"Normalizing {len(sq_orders)} Square orders...")
    for order in sq_orders:
        if order.line_items:
            for line_item in order.line_items:
                date = sf.formatDate(order.created_at, sf.TransactionPlatform.Square)
                transaction_platform = sf.TransactionPlatform.Square
                t_shirt_type = sf.ItemType.fromSquare(line_item.name)
                size = sf.Size.fromSquare(line_item.variation_name)
                retail_price = float(line_item.gross_sales_money.amount / 100)
                earnings = sf.getEarnings(retail_price, sf.TransactionPlatform.Square)
                comments = "Generated from Square API and jamn_sales_tracker"

                entry = sf.generateRowsData(date, transaction_platform, t_shirt_type, size, retail_price, earnings, comments)
                all_sales.append(entry)
        else:
            # uncatagorized transaction
            date = sf.formatDate(order.created_at, sf.TransactionPlatform.Square)
            transaction_platform = sf.TransactionPlatform.Square
            t_shirt_type = sf.ItemType.Unknown
            size = sf.Size.Unknown
            retail_price = float(order.total_money.amount or 0) / 100 if order.total_money else 0.0
            earnings = sf.getEarnings(retail_price, sf.TransactionPlatform.Square)
            comments = "Generated from Square API and jamn_sales_tracker"

            entry = sf.generateRowsData(date, transaction_platform, t_shirt_type, size, retail_price, earnings, comments)
            all_sales.append(entry)

    # For Venmo, fetch recent transactions
    print("Fetching sales data from Venmo...")
    vm_orders = [] # vm_client.get_transactions(limit=50)
    print(f"Normalizing {len(vm_orders)} Venmo orders...") 
    for order in vm_orders:
        print(order) # TODO - debug

        date = "???"
        transaction_platform = sf.TransactionPlatform.Venmo
        t_shirt_type = sf.ItemType.fromVenmo("???")
        size = sf.Size.fromVenmo("???")
        retail_price = 0.0
        earnings = sf.getEarnings(retail_price, sf.TransactionPlatform.Venmo)
        comments = "Generated from Venmo API and jamn_sales_tracker"

        entry = sf.generateRowsData(date, transaction_platform, t_shirt_type, size, retail_price, earnings, comments)
        all_sales.append(entry)

    return all_sales

def log_sales(all_sales):
    print(f"Appending {len(all_sales)} sales to Google Sheets...")

    # TODO - debug
    for row in all_sales:
        print(row)

    gs_client = GoogleSheetsClient(credentials_path=os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
    # gs_client.append_rows(spreadsheet_id=os.getenv('GOOGLE_SHEET_ID'), rows=all_sales)

    print(f"Successfully logged {len(all_sales)} sales.")

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    
    print("JAMN Sales Tracker Initialized.")
    all_sales = fetch_sales()
    log_sales(all_sales)
    print("JAMN Sales Tracker Complete.")
