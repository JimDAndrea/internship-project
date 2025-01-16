from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    MAIN_SIGN_IN_BTN = (By.CSS_SELECTOR, "[id='account-sign-in']")
    RT_SIDE_NAV_SIGNIN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_IN_PAGE_SIGNIN_BTN = (By.CSS_SELECTOR, "[@id='login']")
    MAIN_PAGE_HDR = (By.XPATH, "//a[@aria-current='page' and text()='Off-plan']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def ClickCart(self):
        # self.click(*self.CART_ICON)
        self.wait_and_click(*self.CART_ICON)

    def ClickSignIn(self):
        self.click(*self.MAIN_SIGN_IN_BTN)

    def ClickSignInFromNav(self):
        self.click(*self.RT_SIDE_NAV_SIGNIN)

    def VerifySignInForm(self):
        self.verify_text('Sign in', *self.SIGN_IN_PAGE_SIGNIN_BTN)

    def ClickOffPlan(self):
        self.click(*self.MAIN_PAGE_HDR)