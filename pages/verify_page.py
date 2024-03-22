from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class verifypage(Page):
    VERIFIED_SECTION = (By.XPATH, "//div[@class='verified-section']")

    def verify_right_page(self):
        self.wait_element_to_appear(self.VERIFIED_SECTION)
        self.find_element(*self.VERIFIED_SECTION).is_displayed()



