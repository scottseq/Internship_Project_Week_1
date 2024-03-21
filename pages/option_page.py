from selenium.webdriver.common.by import By

from pages.base_page import Page


class optionpage(Page):
    def option_page(self):
        self.find_element(By.XPATH, "//a[@href='/secondary-listings']").click()


