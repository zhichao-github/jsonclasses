from __future__ import annotations
from unittest import TestCase
from jsonclasses.exceptions import ValidationException
from tests.classes.product_name import AlphaAnalysis


class TestIsAlpha(TestCase):

    def test_alpha_doesnt_raise_if_value_is_alpha(self):
        analysis = AlphaAnalysis(product_name='water')
        analysis.validate()

    def test_alpha_raises_if_value_is_value_is_number(self):
        analysis = AlphaAnalysis(product_name='123')
        with self.assertRaises(ValidationException) as context:
            analysis.validate()
        self.assertEqual(len(context.exception.keypath_messages), 1)
        self.assertEqual(context.exception.keypath_messages['product_name'],
                         "product_name '123' at 'product_name' is not a alpha.")

    def test_alpha_raises_if_value_is_value_contain_number(self):
        analysis = AlphaAnalysis(product_name='water12')
        with self.assertRaises(ValidationException) as context:
            analysis.validate()
        self.assertEqual(len(context.exception.keypath_messages), 1)
        self.assertEqual(context.exception.keypath_messages['product_name'],
                         "product_name 'water12' at 'product_name' is not a alpha.")

    def test_alpha_raises_if_value_is_value_with_special_character(self):
        analysis = AlphaAnalysis(product_name='water!')
        with self.assertRaises(ValidationException) as context:
            analysis.validate()
        self.assertEqual(len(context.exception.keypath_messages), 1)
        self.assertEqual(context.exception.keypath_messages['product_name'],
                         "product_name 'water!' at 'product_name' is not a alpha.")