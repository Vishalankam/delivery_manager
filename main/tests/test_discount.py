import unittest
from ..models.Discount import Discount


class TestDiscount(unittest.TestCase):

    def test_delivery_cost(self):
        self.assertEqual(Discount.get_the_delivery_cost(
            self, 100, 120, 100), 1800)

    def test_discount(self):
        self.assertEqual(Discount.get_discount(
            self, 1800, 75, 75, "OFR001"), 180)
