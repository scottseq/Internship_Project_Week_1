from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class loginpage(Page):

    def login(self):
        self.input_text('sequirascott@gmail.com', *self.username)
        self.input_text('$eQuira1', *self.password)
        self.click(*self.button)
        sleep(6)

    # def login(self):
    # self.input_text(text:'sequirascott@gmail.com', *locator: *self.username
    # self.input_text(*self text:'$eQuira1',*locator: 'password')
    # self.click(*self.button)
    # sleep(6)
