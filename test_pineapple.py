import unittest
from pineapple import Pineapple

class TestPineapple(unittest.TestCase):
    def test_taste(self):
        p = Pineapple("Test", "Sweet", 1.0)
        self.assertIn("tastes", p.taste())

if __name__ == "__main__":
    unittest.main()
