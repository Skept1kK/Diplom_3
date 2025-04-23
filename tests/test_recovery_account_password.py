import allure
from conftest import *
from page.main_page import MainPage
from page.recovery_password_page import RecoveryPage


class TestPasswdRecoveryPage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_switch_to_recovery_password(self, driver):
        main_page = MainPage(driver)
        recovery_password_page = RecoveryPage(driver)
        main_page.click_on_button_login()
        recovery_password_page.click_password_reset_link()
        assert recovery_password_page.check_displaying_of_input_email()


    @allure.title('Проверка ввода почты в поле "email')
    def test_enter_email_to_recovery_password(self, driver):
        main_page = MainPage(driver)
        recovery_password_page = RecoveryPage(driver)
        main_page.click_on_button_login()
        recovery_password_page.click_password_reset_link()
        recovery_password_page.set_email_for_reset_password()
        recovery_password_page.click_on_recovery_button()
        assert recovery_password_page.check_displaying_of_save_button


    @allure.title('Проверка активации поля ввода пароля')
    def test_activated_password_field(self, driver):
        main_page = MainPage(driver)
        recovery_password_page = RecoveryPage(driver)
        main_page.click_on_button_login()
        recovery_password_page.click_password_reset_link()
        recovery_password_page.set_email_for_reset_password()
        recovery_password_page.click_on_recovery_button()
        recovery_password_page.click_on_eye_icon()
        assert recovery_password_page.find_input_active

