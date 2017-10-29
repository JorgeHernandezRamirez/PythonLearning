import unittest

from google.V4GoogleSheetsDriver import V4GoogleSheetsDriver

class GoogleSheetsApi(unittest.TestCase):

    _SPREADSHEETID = '1IH15873lokOM8JvTAz8_NxQCI57IdlLLodKU_QXB5Kk'

    @classmethod
    def setUpClass(cls):
        cls._v4GoogleSheetsDriver = V4GoogleSheetsDriver(V4GoogleSheetsDriver.getCredentials(), cls._SPREADSHEETID)

    def test_shouldBeNotNullV4GoogleSheetsDrive(self):
        self.assertIsNotNone(self._v4GoogleSheetsDriver)

    def test_shouldSetAndGetValuesFromMyGoogleSheet(self):
        self._v4GoogleSheetsDriver.setRange("Sheet1!A1:C1", [["Nombre1", "Apellidos1", "Edad1"]])
        self.assertEqual([["Nombre1", "Apellidos1", "Edad1"]], self._v4GoogleSheetsDriver.getRange("Sheet1!A1:C1"))

    def test_shouldSetAndGetValuesFromNewGoogleSheetsDriver(self):
        v4GoogleSheetsDriver = V4GoogleSheetsDriver(V4GoogleSheetsDriver.getCredentials())
        spreadsheetId = v4GoogleSheetsDriver.createSpreedSheet("Test sheet")
        newV4GoogleSheetsDriver = V4GoogleSheetsDriver(V4GoogleSheetsDriver.getCredentials(), spreadsheetId)
        newV4GoogleSheetsDriver.setRange("Sheet1!A1:C1", [["Nombre1", "Apellidos1", "Edad1"]])
        self.assertEqual([["Nombre1", "Apellidos1", "Edad1"]], newV4GoogleSheetsDriver.getRange("Sheet1!A1:C1"))
        self.assertEqual(1, len(newV4GoogleSheetsDriver.getSheets()))
        self.assertEqual("Sheet1", newV4GoogleSheetsDriver.getSheets()[0].get("properties").get("title"))

    def test_shouldCreateAndDeleteSheetFromNewGoogleSheets(self):
        v4GoogleSheetsDriver = V4GoogleSheetsDriver(V4GoogleSheetsDriver.getCredentials())
        spreadsheetId = v4GoogleSheetsDriver.createSpreedSheet("Mi Test Spreedsheets")
        newV4GoogleSheetsDriver = V4GoogleSheetsDriver(V4GoogleSheetsDriver.getCredentials(), spreadsheetId)
        newV4GoogleSheetsDriver.createSheet("Mi Nueva Hoja")
        self.assertEqual(2, len(newV4GoogleSheetsDriver.getSheets()))
        sheetId = self._getSheetIdFromSheetName(newV4GoogleSheetsDriver, "Mi Nueva Hoja")
        newV4GoogleSheetsDriver.deleteSheet(sheetId)
        self.assertEqual(1, len(newV4GoogleSheetsDriver.getSheets()))

    def _getSheetIdFromSheetName(self, googleSheetsDriver, sheetName):
        sheetListProperties = list(filter(lambda sheetProperties: sheetName == sheetProperties.get("properties").get("title"), googleSheetsDriver.getSheets()))
        if len(sheetListProperties) == 1:
            return sheetListProperties[0].get("properties").get("sheetId")
        return None

if __name__ == "__main__":
    unittest.main()
