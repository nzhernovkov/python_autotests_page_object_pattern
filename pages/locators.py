from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "[href*='basket']")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_REPEAT_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '.alert-success:first-child strong')
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
