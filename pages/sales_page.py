from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from features.steps.seconday_deals import FORSALE, CARD
from pages.base_page import Page
from time import sleep


class salespage(Page):
    FORSALE = (By.XPATH, "//div[@text='For sale']")
    CARD = (By.XPATH, "//div[@class='listing-card']")

    def verify_all_cards(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        #wait.until
        #sleep(2)

        all_tags = self.driver.find_elements(*CARD)

        for tags in all_tags:
            title = tags.find_element(*FORSALE).text
            print('All Tagged')
            assert title, 'Not for Sale'
