import allure
from conftest import *
from page.main_page import MainPage
from page.personal_account_page import AccountPage


class TestAccountPage:

    @allure.title('Проверка перехода в личный кабинет пользователя ')
    def test_switch_to_account_page(self, driver):
        main_page = MainPage(driver)
        personal_account_page = AccountPage(driver)
        main_page.click_on_button_login()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.set_email_field()
        personal_account_page.set_password_field()
        personal_account_page.click_login_button()
        personal_account_page.click_on_personal_account_button()
        assert personal_account_page.check_on_order_history_button


    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_switch_to_order_history(self, driver):
        main_page = MainPage(driver)
        personal_account_page = AccountPage(driver)
        main_page.click_on_button_login()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.set_email_field()
        personal_account_page.set_password_field()
        personal_account_page.click_login_button()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_order_history_button()
        assert personal_account_page.check_on_order_history


    @allure.title('Проверка выхода из аккаунта')
    def test_logout_from_account(self, driver):
        main_page = MainPage(driver)
        personal_account_page = AccountPage(driver)
        main_page.click_on_button_login()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.set_email_field()
        personal_account_page.set_password_field()
        personal_account_page.click_login_button()
        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_logout_button()
        assert personal_account_page.wait_visibility_of_button_register