import os
from playwright.sync_api import sync_playwright

def run_tests():
    html_path = 'file://' + os.path.abspath('calc.html')
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path)

        display = page.locator('#display')
        assert display.input_value() == '', 'Initial display should be empty'

        # Test digit clicking: 1, 2, 3
        page.locator('button[data-val="1"]').click()
        page.locator('button[data-val="2"]').click()
        page.locator('button[data-val="3"]').click()
        assert display.input_value() == '123', f'Expected 123, got {display.input_value()}'

        # Test operator: +
        page.locator('button[data-val="+"]').click()
        assert display.input_value() == '123+', f'Expected 123+, got {display.input_value()}'

        # Test digit: 7
        page.locator('button[data-val="7"]').click()
        assert display.input_value() == '123+7', f'Expected 123+7, got {display.input_value()}'

        # Test calculate: =
        page.locator('button[data-action="calculate"]').click()
        assert display.input_value() == '130', f'Expected 130, got {display.input_value()}'

        # Test clear: c
        page.locator('button[data-action="clear"]').click()
        assert display.input_value() == '', f'Expected empty, got {display.input_value()}'

        # Test decimal and multiply: 2.5 * 4 = 10
        page.locator('button[data-val="2"]').click()
        page.locator('button[data-val="."]').click()
        page.locator('button[data-val="5"]').click()
        page.locator('button[data-val="*"]').click()
        page.locator('button[data-val="4"]').click()
        page.locator('button[data-action="calculate"]').click()
        assert display.input_value() == '10', f'Expected 10, got {display.input_value()}'

        # Test division: / 2 = 5
        page.locator('button[data-val="/"]').click()
        page.locator('button[data-val="2"]').click()
        page.locator('button[data-action="calculate"]').click()
        assert display.input_value() == '5', f'Expected 5, got {display.input_value()}'

        # Test invalid syntax / error handling: + = should clear currentvalue
        page.locator('button[data-action="clear"]').click()
        page.locator('button[data-val="+"]').click()
        page.locator('button[data-action="calculate"]').click()
        assert display.input_value() == '', f'Expected empty on error, got {display.input_value()}'

        # Verify result on additional sequence
        page.locator('button[data-val="4"]').click()
        page.locator('button[data-val="2"]').click()
        assert display.input_value() == '42', f'Expected 42, got {display.input_value()}'

        browser.close()
        print('All tests passed successfully!')

if __name__ == '__main__':
    run_tests()
