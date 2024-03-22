from selenium.webdriver.common.by import By


from pages.base_page import Page


class productspage(Page):
    # FILTER_TAG = (By.XPATH, "//div[@class='filter-text']")
    # FILTER_TAG2 = (By.XPATH, "//div[@class='tag-text-filters']")
    # FILTER_TAG3 = (By.XPATH, "//a[@class='button-filter w-button']")

    def verify_products_page(self):
        self.wait_element_clickable_click(self.FILTER_TAG)
        self.wait_element_clickable_click(self.FILTER_TAG2)
        self.wait_element_clickable_click(self.FILTER_TAG3)

        # self.find_element(By.XPATH, "//div[@class='tag-text-filters']").click()
        # self.find_element(By.XPATH, "//a[@class='button-filter w-button']").click()
