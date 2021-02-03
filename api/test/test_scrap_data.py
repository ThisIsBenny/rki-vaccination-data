""" Unittest """
import unittest
# pylint: disable=import-error
from _utils import scrap_data

class TestModuleScrapData(unittest.TestCase):
  """ Test Module """
  def test_get_file(self):
    """ Test for scrap_data.get_file """
    self.assertEqual(type(scrap_data.get_file()).__name__, "bytes")
  def test_get_data(self):
    """ Test for scrap_data.get_data """
    data = scrap_data.get_data()
    self.assertEqual(type(data).__name__, "dict")

    self.assertIn("lastUpdate", data.keys())
    self.assertIn("states", data.keys())
    self.assertIn("sumStates", data.keys())
    self.assertIn("sumStates2nd", data.keys())
    self.assertIn("sumDiffStates", data.keys())
    self.assertIn("sumDiffStates2nd", data.keys())
    self.assertIn("totalGermany", data.keys())

    self.assertEqual(type(data["lastUpdate"]).__name__, "datetime")
    self.assertEqual(type(data["states"]).__name__, "dict")
    self.assertEqual(type(data["sumStates"]).__name__, "int")
    self.assertEqual(type(data["sumStates2nd"]).__name__, "int")
    self.assertEqual(type(data["sumDiffStates"]).__name__, "int")
    self.assertEqual(type(data["sumDiffStates2nd"]).__name__, "int")
    self.assertEqual(type(data["totalGermany"]).__name__, "int")

if __name__ == '__main__':
  unittest.main()
