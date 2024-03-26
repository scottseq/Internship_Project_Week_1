from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from features.steps.seconday_deals import FORSALE, CARD
from pages.base_page import Page
from time import sleep


class salespage(Page):
    FORSALE = (By.XPATH, "//div[@wized='saleTagMLS']")
    CARD = (By.XPATH, "//div[@class='listing-card']")

    def verify_all_cards(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        all_tags = self.find_elements(*self.CARD)
        print('total tags:', len(all_tags))

        for tags in all_tags:
            self.wait_element_to_appear(*self.FORSALE)
            title = tags.find_element(*self.FORSALE).text
            print('Tag: ' + title)
            assert title, 'Not for Sale'
