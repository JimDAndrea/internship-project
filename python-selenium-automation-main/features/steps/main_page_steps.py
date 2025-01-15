from selenium.webdriver.common.by import By
from behave import given, when, then

#CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
#ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
#ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIGN_IN_EMAIL= 'jamesgregorydandrea@hotmail.com'
SIGN_IN_PASSWORD = 'Reelly'
SIGN_IN_WITH_BTN = (By.XPATH, "//a[@wized='loginButton']")


@given('Open Reelly main page')
def open_main(context):
    context.app.main_page.open_main()

@then('Input email on SignIn page')
def input_email(context):
    context.app.login_page.InputEmail(SIGN_IN_EMAIL)

@then('Input password on SignIn page')
def input_password(context):
    context.app.login_page.InputPassword('jirasoftware')

@then('Click Continue Button')
def VerifyUserLoggedIn(context):
    self.driver.find_element(*SIGN_IN_WITH_BTN).click()
    #context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn

@then('Verify Main Page Open')
def VerifyMainPageOpen(context):
    self.driver.find_element(*SIGN_IN_WITH_BTN).click()





