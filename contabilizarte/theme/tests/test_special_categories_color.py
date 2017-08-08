import unittest
from contabilizarte.theme.templatetags.speciallinks import (
    CATEGORIES_COLOR_ORDERING,
    gen_category_color,
    next_color,
    get_color,
)


class SpecialCategoriesColorTest(unittest.TestCase):
    def test_order_colors(self):
        self.assertEqual(
            ['laranja', 'azul', 'verde', 'amarelo'],
            CATEGORIES_COLOR_ORDERING
        )

    def test_colors_hex(self):
        self.assertEqual('#f74c00', get_color('laranja'))
        self.assertEqual('#46c9dd', get_color('azul'))
        self.assertEqual('#3fe525', get_color('verde'))
        self.assertEqual('#fff200', get_color('amarelo'))
