""" Unittest """
import unittest
# pylint: disable=import-error
from _utils import scrap_data_v2

class TestModuleScrapData(unittest.TestCase):
  """ Test Module """
  def test_get_file(self):
    """ Test for scrap_data_v2.get_file """
    self.assertEqual(type(scrap_data_v2.get_file()).__name__, "bytes")
  def test_get_data(self):
    """ Test for scrap_data_v2.get_data """
    data = scrap_data_v2.get_data()
    self.assertEqual(type(data).__name__, "dict")

    self.assertIn("lastUpdate", data.keys())
    self.assertIn("data", data.keys())

    self.assertEqual(type(data["lastUpdate"]).__name__, "datetime")
    self.assertEqual(type(data["data"]).__name__, "dict")

if __name__ == '__main__':
  unittest.main()
