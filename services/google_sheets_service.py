import gspread

class GoogleSheetsClient:
    """
    A client to interact with Google Sheets API using a service account.
    """
    def __init__(self, credentials_path):
        # Authenticate using the service account file path
        self.client = gspread.service_account(filename=credentials_path)

    def append_rows(self, spreadsheet_id, rows):
        """
        Appends multiple rows to the first worksheet of the specified spreadsheet.
        
        :param spreadsheet_id: The ID of the spreadsheet (found in the URL).
        :param rows: A list of lists representing rows of data.
        """
        # Open the spreadsheet by its ID
        spreadsheet = self.client.open_by_key(spreadsheet_id)
        # Select the first sheet (index 0)
        worksheet = spreadsheet.get_worksheet(0)
        return worksheet.append_rows(rows)