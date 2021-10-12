from __future__ import annotations
from tests.classes.simple_calculation import SimpleCalculation
from unittest import TestCase

class TestMod(TestCase):

    def test_mod_with_int_value_mods_original_value(self):
        mod_int = SimpleCalculation(i_mod=8)
        self.assertEqual(mod_int.i_mod, 3)

    def test_mod_with_float_value_mods_original_value(self):
        mod_float = SimpleCalculation(f_mod=8.5)
        self.assertEqual(mod_float.f_mod, 1)
