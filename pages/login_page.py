from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from time import sleep

class SignInPage(BasePage):

    SIGN_IN_EMAIL = (By.CSS_SELECTOR, "[id*='email-2']")
    SIGN_IN_PASSWORD = (By.CSS_SELECTOR, "[id*='field']")
    SIGN_IN_WITH_BTN = (By.XPATH, "//a[@wized='loginButton']")

    def InputEmail(self, email):
        sleep(3)
        self.input_text(email, *self.SIGN_IN_EMAIL)

    def InputPassword(self, password):
        sleep(2)
        self.input_text(password,*self.SIGN_IN_PASSWORD)

    def VerifyUserLoggedIn(self):
        sleep(2)
        self.driver.find_element(*self.SIGN_IN_WITH_BTN).click()