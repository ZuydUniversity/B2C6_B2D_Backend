import unittest



def sum_numbers(a, b):
  return a + b

class test(unittest.TestCase):

  def test_sum_positive_numbers(self):
    """Test het optellen van twee positieve getallen."""
    self.assertEqual(sum_numbers(1, 2), 3)

  def test_sum_negative_numbers(self):
    """Test het optellen van twee negatieve getallen."""
    self.assertEqual(sum_numbers(-1, -2), -3)

  def test_sum_zero(self):
    """Test het optellen van een getal met nul."""
    self.assertEqual(sum_numbers(1, 0), 1)

if __name__ == "__main__":
    unittest.main()
