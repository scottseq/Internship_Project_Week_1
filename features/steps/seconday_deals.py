from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

username = "sequirascott@gmail.com"
password = "$eQuira1"
FORSALE = (By.XPATH, "//div[@wized='saleTagMLS']")
OPTION = (By.XPATH, "//div[@class='verified-section']")
VERIFYPAGE = (By.XPATH, "//div[@class='verified-section']")
CARD = (By.XPATH, "//div[@class='listing-card']")



@given('Open the main page')
def open_main_page(context):
    #context.driver.get('https://soft.reelly.io/')
    context.app.main_page.open_main_page()

@then('Log in to the page')
def login(context):
    #context.driver.find_element(By.ID, 'email-2').send_keys(username)
    #context.driver.find_element(By.ID, 'field').send_keys(password)
    #context.driver.find_element(By.CSS_SELECTOR, 'a[class = "login-button w-button"]').click()
    context.app.login_page.login()
    #print('Logged in Successfully')
    #sleep(3)


@when('Click on "secondary" option at the left side of the page')
def click_secondary(context):
    #context.driver.find_element(By.XPATH, "//a[@href='/secondary-listings']").click()
    context.app.option_page.option_page()

@then('Verify the right page opens')
def verify_right_page(context):
    #context.driver.find_element(By.XPATH, "//div[@class='verified-section']").is_displayed()
    #print('Correct page opened')
    context.app.verify_page.verify_right_page()

@when('Filter the products by "want to sell"')
def filter_products(context):
    #context.driver.find_element(By.XPATH, "//div[@class='filter-text']").click()
    #context.driver.find_element(By.XPATH, "//div[@class='tag-text-filters']").click()
    #context.driver.find_element(By.XPATH, "//a[@class='button-filter w-button']").click()
    context.app.products_page.verify_products_page()


TAG = (By.XPATH, "//div[@text='for-sale-tag'")
@then('Verify all cards have "for sale" tag')
def verify_all_cards(context):
    #context.driver.execute_script("window.scrollBy(0,2000)", "")
    #sleep(2)

    #all_tags = context.driver.find_elements(*CARD)

    #for tags in all_tags:

        #title = tags.find_element(*FORSALE).text
        #print('All Tagged')
        #assert title, 'Not for Sale'verify_all_cards(context):
    context.app.sales_page.verify_all_cards()





    #actual_text = context.driver.find_element(FORSALE).text
    #assert 'for sale' in actual_text, f'Expected "for sale", but got {actual_text}'
    #print('Test case passed')
    #context.app.sales_page.verify_all_cards()