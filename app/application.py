from pages.main_page import mainpage
from pages.option_page import OptionPage
from pages.products_page import productspage
from pages.sales_page import salespage
from pages.login_page import loginpage
from pages.base_page import Page
from pages.verify_page import verifypage


class Application:

    def __init__(self, driver):
        self.option_page = OptionPage(driver)
        self.main_page = mainpage(driver)
        self. products_page = productspage(driver)
        self.sales_page = salespage(driver)
        self.login_page = loginpage(driver)
        self.base_page = Page(driver)
        self.verify_page = verifypage(driver)
