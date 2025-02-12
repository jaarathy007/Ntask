import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 3), 5)

   def test_subtract(self):
       self.assertEqual(subtract(10, 4), 6)

   def test_multiply(self):
       self.assertEqual(multiply(3, 3), 9)

   def test_divide(self):
       self.assertEqual(divide(10, 2), 5)
       with self.assertRaises(ValueError):
           divide(10, 0)

if __name__ == "__main__":
   unittest.main()
