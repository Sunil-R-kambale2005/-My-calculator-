import os
from playwright.sync_api import sync_playwright

def run_tests():
    html_path = "file://" + os.path.abspath("calc.html")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path)

        display = page.locator("#display")
        assert display.input_value() == "", "Initial display should be empty"

        # Test addition: 12 + 34 = 46
        page.click('button[data-val="1"]')
        page.click('button[data-val="2"]')
        page.click('button[data-val="+"]')
        page.click('button[data-val="3"]')
        page.click('button[data-val="4"]')
        assert display.input_value() == "12+34"
        page.click('button[data-action="calculate"]')
        assert display.input_value() == "46", f"Expected 46, got {display.input_value()}"

        # Test clear
        page.click('button[data-action="clear"]')
        assert display.input_value() == "", f"Expected empty, got {display.input_value()}"

        # Test multiplication: 7 * 8 = 56
        page.click('button[data-val="7"]')
        page.click('button[data-val="*"]')
        page.click('button[data-val="8"]')
        page.click('button[data-action="calculate"]')
        assert display.input_value() == "56", f"Expected 56, got {display.input_value()}"

        # Test division: 56 / 2 = 28
        page.click('button[data-val="/"]')
        page.click('button[data-val="2"]')
        page.click('button[data-action="calculate"]')
        assert display.input_value() == "28", f"Expected 28, got {display.input_value()}"

        # Test subtraction: 28 - 9 = 19
        page.click('button[data-val="-"]')
        page.click('button[data-val="9"]')
        page.click('button[data-action="calculate"]')
        assert display.input_value() == "19", f"Expected 19, got {display.input_value()}"

        # Test decimal and 0: 0.5 * 4 = 2
        page.click('button[data-action="clear"]')
        page.click('button[data-val="0"]')
        page.click('button[data-val="."]')
        page.click('button[data-val="5"]')
        page.click('button[data-val="*"]')
        page.click('button[data-val="4"]')
        page.click('button[data-action="calculate"]')
        assert display.input_value() == "2", f"Expected 2, got {display.input_value()}"

        # Test error handling (e.g. invalid syntax: 5 + * 2)
        page.click('button[data-action="clear"]')
        page.click('button[data-val="5"]')
        page.click('button[data-val="+"]')
        page.click('button[data-val="*"]')
        page.click('button[data-val="2"]')
        page.click('button[data-action="calculate"]')
        assert display.input_value() == "", f"Expected empty on error, got {display.input_value()}"

        # Test clicking container outside buttons does not alter display
        page.click('button[data-val="9"]')
        page.click('.btn-container', position={"x": 5, "y": 5})
        assert display.input_value() == "9", f"Expected 9, got {display.input_value()}"

        browser.close()
    print("All calculator tests passed successfully!")

if __name__ == "__main__":
    run_tests()
