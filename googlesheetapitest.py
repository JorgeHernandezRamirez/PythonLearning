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
        idSheet = v4GoogleSheetsDriver.createSheet("Test sheet")
        newV4GoogleSheetsDriver = V4GoogleSheetsDriver(V4GoogleSheetsDriver.getCredentials(), idSheet)
        newV4GoogleSheetsDriver.setRange("Sheet1!A1:C1", [["Nombre1", "Apellidos1", "Edad1"]])
        self.assertEqual([["Nombre1", "Apellidos1", "Edad1"]], newV4GoogleSheetsDriver.getRange("Sheet1!A1:C1"))
        self.assertEqual(1, len(newV4GoogleSheetsDriver.getSheets()))
        self.assertEqual("Sheet1", newV4GoogleSheetsDriver.getSheets()[0].get("properties").get("title"))

if __name__ == "__main__":
    unittest.main()
