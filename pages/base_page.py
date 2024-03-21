from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep




class Page:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, 'email-2')
        self.password = (By.ID, 'field')
        self.button = (By.CSS_SELECTOR, 'a[class = "login-button w-button"]')
        self.FORSALE = (By.XPATH, "//div[@text='For sale']")
        self.OPTION = (By.XPATH, "//div[@class='verified-section']")
        self.VERIFYPAGE = (By.XPATH, "//div[@class='verified-section']")
        self.FORSALE = (By.XPATH, "//div[@text='For sale']")
        self.CARD = (By.XPATH, "//div[@class='listing-card']")



    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is clickable'
        )

    def wait_element_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is clickable').click()

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f"Expected '{expected_text}' not in '{actual_text}'"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected '{expected_url}' but got '{actual_url}'"

    def enter_username(self, username):
        self.driver.find_element_by_id('username').send_keys('sequirascott@gmail.com')

    def enter_password(self, password):
        self.driver.find_element_by_id('password').send_keys('$eQuira1')

    def click_login_button(self):
        self.driver.find_element(self.button).click()


