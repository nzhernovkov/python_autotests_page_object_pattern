import time

import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.should_be_added_product()


@pytest.mark.parametrize('url_param', ["?promo=offer0",
                                       "?promo=offer1",
                                       "?promo=offer2",
                                       "?promo=offer3",
                                       "?promo=offer4",
                                       "?promo=offer5",
                                       "?promo=offer6",
                                       pytest.param(
                                           "?promo=offer7",
                                           marks=pytest.mark.xfail),
                                       "?promo=offer8",
                                       "?promo=offer9"])
def test_guest_can_add_product_to_basket_on_promo_pages(browser, url_param):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{url_param}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_product()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.go_to_login_page()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_added_product()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappear_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_success_message_disappear()
