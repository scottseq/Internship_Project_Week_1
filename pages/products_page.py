from selenium.webdriver.common.by import By


from pages.base_page import Page


class productspage(Page):
    def verify_products_page(self):
        self.find_element(By.XPATH, "//div[@class='filter-text']").click()
        self.find_element(By.XPATH, "//div[@class='tag-text-filters']").click()
        self.find_element(By.XPATH, "//a[@class='button-filter w-button']").click()
