""" Unittest """
import unittest
from _utils import scrap_data

class TestModule(unittest.TestCase):
  """ Test Module """
  def test_get_file(self):
    """ Test for scrap_data.get_file """
    self.assertTrue(type(scrap_data.get_file()).__name__ == "bytes")

if __name__ == '__main__':
  unittest.main()
