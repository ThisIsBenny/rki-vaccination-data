""" Unittest """
import unittest
# pylint: disable=import-error
from _utils.statics import inhabitants

class TestModuleStaticsInhabitants(unittest.TestCase):
  """ Test Module for statics.inhabitants """
  def test_total(self):
    """ Test for inhabitants.TOTAL """
    self.assertEqual(type(inhabitants.TOTAL).__name__, "int")

  def test_states(self):
    """ Test for inhabitants.STATES """
    self.assertEqual(type(inhabitants.STATES).__name__,"dict")

if __name__ == '__main__':
  unittest.main()
