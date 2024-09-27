import unittest
from add import mul

class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mul(1, 2), 2)

if __name__ == '__main__':
    unittest.main()
