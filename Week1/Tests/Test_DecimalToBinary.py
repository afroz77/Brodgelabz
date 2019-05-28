from Week1.Util import Decimal_To_Binary
from unittest import TestCase
import unittest


class Test_Decimal_to_Binary(TestCase):

    def Test_BinaryOf100(self):
        result = Decimal_To_Binary(100)
        expected = "1100100"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()