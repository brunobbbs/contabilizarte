import unittest
from contabilizarte.theme.templatetags.speciallinks import CATEGORIES_COLOR_ORDERING


class SpecialCategoriesColorTest(unittest.TestCase):
    def test_order_colors(self):
        self.assertEqual(
            ['laranja', 'azul', 'verde', 'amarelo'],
            CATEGORIES_COLOR_ORDERING
        )
