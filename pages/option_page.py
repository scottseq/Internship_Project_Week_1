from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class OptionPage(Page):
    SECONDARY2 = (By.XPATH, "//div[@class='menu-button-text']")
    SECONDARY = (By.CSS_SELECTOR, '[href="/secondary-listings"] [class="menu-button-text"]')

    def option_page(self, *locator):
        #self.click(*self.SECONDARY)
        self.wait.until(EC.visibility_of_element_located(self.SECONDARY),
                        message=f'Could not find {self.SECONDARY} locator for {locator}'
                        ).click()

         #self.find_element(self.SECONDARY2)
         #self.find_element(self.SECONDARY2).click()
         #self.wait_element_clickable(self.SECONDARY2)
         #self.click(self.SECONDARY)

