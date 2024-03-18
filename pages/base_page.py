from selenium.webdriver import Keys



    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)


    def find_element(self, *locator):
        self.driver.find_element(*locator)


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def inpuy_text(self, text,  *locator):
        self.driver.find_element(*locator).send_keys(text)