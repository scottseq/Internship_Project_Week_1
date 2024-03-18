from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



username = ("sequirascott@gmail.com")
password = ("$eQuira1")


@given ('Open the main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io/')


@given('Log in to the page')
def login(context):
        context.driver.findlelement(By. ID, ('email-2').send_keys(username))
        context.driver.findlelement(By. ID, ('field').send_keys(password))
        context.driver.findlelement(By. CSS_SELECTOR, (input['.login-button w-button']).click())

        print('Logged in Successfully')
        sleep(3)



@when('Click on "secondary" option at the left side of the page')
def click_secondary(context):
    context.driver.find_element (By. CSS, ['.class= menu-button-block']).click()


@then('Verify the right page opens')
def verify_right_page(context):
    context.driver.find_element(By.CSS_SELECTOR, ('[.verified-contaier w-container]').is_displayed())
    print('Correct page opened')

@when('Filter the products by "want to sell"')
def filter_products(context):
    context.driver. find_element(By.CSS_SELECTOR, ('filter-button').click()
    context.driver.find_element(By.CSS_SELECTOR, (['.tag-text-filters']).click())
    context.driver.find_element(By. CSS_SELECTOR, (['.button-filter w-button']).click())



@then('Verify all cards have "for sale" tag')
def verify_all_cards(context):
    actual_text = context.find_element(By.CSS_SELECTOR, '[.for-sale-block]').text
    assert 'for sale' in actual_text, f'Expected: {"for sale"}, Actual: {actual_text}'
    print('Test case passed')


