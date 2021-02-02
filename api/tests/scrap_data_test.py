""" Unittest """
import unittest
from _utils import scrap_data

class TestModule(unittest.TestCase):
  """ Test Module """
  def test_get_file(self):
    """ Test for scrap_data.get_file """
    self.assertTrue(type(scrap_data.get_file()).__name__ == "bytes")
  def test_get_data(self):
    """ Test for scrap_data.get_data """
    self.assertTrue(type(scrap_data.get_data()).__name__ == "dict")

if __name__ == '__main__':
  unittest.main()
