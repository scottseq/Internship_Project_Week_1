from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class loginpage(Page):


    def __init__(self, driver):
        super().__init__(driver)
        # self.wait = None

    def login(self):
        self.wait_element_to_appear(*self.username)
        self.input_text('sequirascott@gmail.com', *self.username)
        self.wait_element_to_appear(*self.password)
        self.input_text('$eQuira1', *self.password)
        self.wait_element_clickable_click(*self.button)





