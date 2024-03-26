from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class verifypage(Page):
    VERIFIED_SECTION = (By.XPATH, "//div[@class='verified-section']")
    VERIFIED_SECTION2 = (By.CSS_SELECTOR, '.verified-section')

    def verify_right_page(self):
        self.wait_element_to_appear(*self.VERIFIED_SECTION2)
        #self.display(self.VERIFIED_SECTION2)



