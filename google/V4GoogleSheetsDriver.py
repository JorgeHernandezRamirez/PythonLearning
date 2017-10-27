import os

import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from google.AbstractGoogleSheetsDriver import AbstractGoogleSheetsDrive


class V4GoogleSheetsDriver(AbstractGoogleSheetsDrive):

    _SHEETS = 'sheets'

    _V4 = 'v4',

    _DISCOVERYURL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'

    _SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

    _CLIENT_SECRET_FILE = 'client_secret.json'

    _APPLICATION_NAME = 'Google Sheets API Python Quickstart'

    def __init__(self, credentials, spreadsheetId = None):
        super(V4GoogleSheetsDriver, self).__init__(credentials)
        self._spreadsheetId = spreadsheetId
        self._serviceSheetApi = self._createGoogleApiService(credentials)

    def _createGoogleApiService(self, credentials):
        http = credentials.authorize(httplib2.Http())
        return discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=(self._DISCOVERYURL))

    def createSpreedSheet(self, docname):
        spreadsheet_body = {"properties": {"title": docname}}
        return self._serviceSheetApi.spreadsheets().create(body=spreadsheet_body).execute().get('spreadsheetId')

    def getRange(self, range):
        result = self._serviceSheetApi.spreadsheets().values().get(spreadsheetId=self._spreadsheetId, range=range).execute()
        return result.get('values', [])

    def setRange(self, range, values):
        requestBody = {'values': values}
        self._serviceSheetApi.spreadsheets().values().update(
            spreadsheetId=self._spreadsheetId, valueInputOption="RAW", range=range, body=requestBody).execute()

    def getSheets(self):
        return self._serviceSheetApi.spreadsheets().get(spreadsheetId=self._spreadsheetId).execute().get("sheets")

    def createSheet(self, title):
        self._serviceSheetApi.spreadsheets().batchUpdate(spreadsheetId=self._spreadsheetId, body=self._getCreateSheetBody(title)).execute()

    def _getCreateSheetBody(self, title):
        return {"requests":[{"addSheet":{"properties":{"title":title}}}]}

    @staticmethod
    def getCredentials():
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'sheets.googleapis.com-python-quickstart.json')
        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(V4GoogleSheetsDriver._CLIENT_SECRET_FILE, V4GoogleSheetsDriver._SCOPES)
            flow.user_agent = V4GoogleSheetsDriver._APPLICATION_NAME
            credentials = tools.run(flow, store)
        return credentials

    @property
    def spreadsheetId(self):
        return self._spreadsheetId;

    @spreadsheetId.setter
    def spreadsheetId(self, _spreadsheetId):
        self._spreadsheetId = _spreadsheetId;
