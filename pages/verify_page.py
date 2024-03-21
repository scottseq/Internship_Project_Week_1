from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class verifypage(Page):

    def verify_right_page(self):
        self.find_element(By.XPATH, "//div[@class='verified-section']").is_displayed()



