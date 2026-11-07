import os
import unittest
from playwright.sync_api import sync_playwright

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()
        cls.calc_url = "file://" + os.path.abspath("calc.html")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.page = self.browser.new_page()
        self.page.goto(self.calc_url)

    def tearDown(self):
        self.page.close()

    def click_buttons(self, tokens):
        for token in tokens:
            if token == 'c':
                self.page.click("button[data-action='clear']")
            elif token == '=':
                self.page.click("button[data-action='calculate']")
            else:
                self.page.click(f"button[data-val='{token}']")

    def test_initial_state(self):
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "")

    def test_digit_input(self):
        self.click_buttons(['1', '2', '3'])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "123")

    def test_addition(self):
        self.click_buttons(['1', '2', '+', '3', '='])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "15")

    def test_subtraction(self):
        self.click_buttons(['9', '-', '4', '='])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "5")

    def test_multiplication(self):
        self.click_buttons(['6', '*', '7', '='])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "42")

    def test_division(self):
        self.click_buttons(['8', '/', '2', '='])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "4")

    def test_decimal(self):
        self.click_buttons(['3', '.', '5', '+', '1', '.', '5', '='])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "5")

    def test_clear(self):
        self.click_buttons(['7', '8', '9'])
        self.click_buttons(['c'])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "")

    def test_chaining(self):
        self.click_buttons(['2', '+', '3', '*', '4', '='])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "14")

    def test_invalid_syntax_error(self):
        self.click_buttons(['+', '*', '='])
        display_val = self.page.input_value("#display")
        self.assertEqual(display_val, "")

if __name__ == "__main__":
    unittest.main()
