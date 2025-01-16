from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
#ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
#ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIGN_IN_EMAIL= '******'
SIGN_IN_PASSWORD = '******'
SIGN_IN_WITH_BTN = (By.XPATH, "//a[@wized='loginButton']")
OFF_PLAN_BTN = (By.XPATH, "//a[text()='Off-plan']")
OFF_PLAN_CSS_BTN = (By.CSS_SELECTOR, '#w-node-b528dfcf-d2ee-f936-302e-86e97f0796e8-7f66df20')
NEXT_PAGE_BTN = (By.XPATH, "//div[text()='Next page']")
PREV_PAGE_BTN = (By.XPATH, "//div[text()='Prev. page']")
CURRENT_PROPERTIES = (By. XPATH, "//div[@wized='currentPageProperties' and @class='page-count']")

@given('Open Reelly main page')
def open_main(context):
    context.app.main_page.open_main()

@then('Input email on SignIn page')
def input_email(context):
    context.app.login_page.InputEmail(SIGN_IN_EMAIL)

@then('Input password on SignIn page')
def input_password(context):
    context.app.login_page.InputPassword(SIGN_IN_PASSWORD)

@then('Click Continue Button')
def VerifyUserLoggedIn(context):
    context.driver.find_element(*SIGN_IN_WITH_BTN).click()
    #context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn

@then('Verify Main Page Open')
def VerifyMainPageOpen(context):
    context.driver.find_element(*SIGN_IN_WITH_BTN).click()
    sleep(5)

@then ('Click off plan option')
def ClickOffPlanOption(context):
    context.driver.wait.until(EC.element_to_be_clickable(OFF_PLAN_CSS_BTN)).click()

@then ('Go to the final page using the pagination button')
def ScrollPagesDown(context):

    context.driver.wait.until(EC.element_to_be_clickable(NEXT_PAGE_BTN)).click()

    current_page_count_element = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@wized='currentPageProperties']")))
    total_page_count_element = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@wized='totalPageProperties']")))
    # Extract the total page count
    current_page_count = int(current_page_count_element.text)
    total_page_count = int(total_page_count_element.text)

    print(f"Total Page Count: {total_page_count}")
    print(f"Current Page Count: {current_page_count}")


    while current_page_count != total_page_count:
                context.driver.wait.until(EC.element_to_be_clickable(NEXT_PAGE_BTN)).click()

                current_page_count_element = context.driver.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@wized='currentPageProperties']")))

                current_page_count = int(current_page_count_element.text)

                total_page_count_element = context.driver.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@wized='totalPageProperties']")))
                # Extract the total page count
                total_page_count = int(total_page_count_element.text)

                print(f"Total Page Count: {total_page_count}")
                print(f"Current Page Count: {current_page_count}")


@then ('Go back to the first page using pagination button')
def ScrollPagesUp(context):

    context.driver.wait.until(EC.element_to_be_clickable(PREV_PAGE_BTN)).click()

    current_page_count_element = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@wized='currentPageProperties']")))
    total_page_count_element = context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@wized='totalPageProperties']")))
    # Extract the total page count
    current_page_count = int(current_page_count_element.text)
    total_page_count = int(total_page_count_element.text)

    print(f"Total Page Count: {total_page_count}")
    print(f"Current Page Count: {current_page_count}")


    while current_page_count != 1:
                context.driver.wait.until(EC.element_to_be_clickable(PREV_PAGE_BTN)).click()

                current_page_count_element = context.driver.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@wized='currentPageProperties']")))

                current_page_count = int(current_page_count_element.text)

                total_page_count_element = context.driver.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@wized='totalPageProperties']")))
                # Extract the total page count
                total_page_count = int(total_page_count_element.text)

                print(f"Total Page Count: {total_page_count}")
                print(f"Current Page Count: {current_page_count}")















