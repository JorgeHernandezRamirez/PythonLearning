#https://developers.google.com/sheets/api/reference/rest
#https://developers.google.com/sheets/api/quickstart/python
from __future__ import print_function

import os

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
#SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1IH15873lokOM8JvTAz8_NxQCI57IdlLLodKU_QXB5Kk'
    rangeName = 'Sheet1!A2:C'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[1]))

    values = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheetId, ranges=["A2:C2", "A3:C3"]).execute()
    for valueRanges in values['valueRanges']:
        for row in valueRanges["values"]:
            print('%s, %s' % (row[0], row[1]))

    values = [
        [
           "Valor1", "Valor2", "Valor3"
        ]
    ]
    body = {
        'values': values
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheetId, valueInputOption="RAW", range="A4:C4", body=body).execute()

    #Añadir valores
    values = [
        [
            "ValorAñadido1", "ValorAñadido2", "ValorAñadido3"
        ]
    ]
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range="Sheet1!A4:C4",
        valueInputOption="RAW", body=body).execute()

    #Obtener todos los sheets
    sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
    for sheet in sheet_metadata.get('sheets'):
        print(sheet.get("properties").get("title"));
        print(sheet.get("properties").get("sheetId"));

    spreadsheet_body = {"properties":{"title":"My new Sheet 1"},"sheets":[{"properties":{"sheetId":0,"title":"Mi Sheet1","index":0,"sheetType":"GRID","gridProperties":{"rowCount":1000,"columnCount":26}}},{"properties":{"sheetId":1,"title":"Mi Sheet2","index":2,"sheetType":"GRID","gridProperties":{"rowCount":1000,"columnCount":26}}}]}
    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()

    requests = []
    requests.append({
        "updateCells": {
            "rows": {
                "values": [
                    {
                        "pivotTable": {
                            "source": {
                                "sheetId": 0,
                                "startRowIndex": 0,
                                "startColumnIndex": 0,
                                "endRowIndex": 10,
                                "endColumnIndex": 3
                            },
                            "rows": [
                                {
                                    "sourceColumnOffset": 0,
                                    "showTotals": True,
                                    "sortOrder": "ASCENDING",
                                },
                            ],
                            "columns": [

                            ],
                            "values": [
                                {
                                    "summarizeFunction": "COUNTA",
                                    "sourceColumnOffset": 1
                                }
                            ],
                            "valueLayout": "HORIZONTAL"
                        }
                    }
                ]
            },
            "start": {
                "sheetId": "1433414668",
                "rowIndex": 0,
                "columnIndex": 0
            },
            "fields": "pivotTable"
        }
    })

    body = {
        'requests': requests
    }
    result = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId,
                                                body=body).execute()

    # TODO: Change code below to process the `response` dict:
    print("Hoja de cálculo creada ", response.get('spreadsheetId'))

    print("End")

if __name__ == '__main__':
    main()