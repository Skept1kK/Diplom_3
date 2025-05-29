import allure

from locator import *
from page.base_page import BasePage
from data import TestData


class RecoveryPage(BasePage):

    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_element(PersonalAccLocators.FORGOT_PASSWORD)

    @allure.step('Проверяем отображение поля email')
    def check_displaying_of_input_email(self):
        self.wait_for_element(RecoveryPasswordLocators.INPUT_EMAIL)
        return self.check_element_display(RecoveryPasswordLocators.INPUT_EMAIL)

    @allure.step('Вводим емейл в поле для восстановления пароля')
    def set_email_for_reset_password(self):
        self.set_value(RecoveryPasswordLocators.INPUT_EMAIL,TestData.LOGIN_NAME)

    @allure.step('Кликаем на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_for_element(RecoveryPasswordLocators.RECOVERY_BUTTON)
        self.click_element(RecoveryPasswordLocators.RECOVERY_BUTTON)

    @allure.step('Проверяем отображение кнопки сохранить')
    def check_displaying_of_save_button(self):
        self.wait_for_element(RecoveryPasswordLocators.SAVE_BUTTON)
        return self.check_element_display(RecoveryPasswordLocators.SAVE_BUTTON)

    @allure.step('Кликаем на иконку глаза в поле ввода пароля')
    def click_on_eye_icon(self):
        self.wait_for_element(RecoveryPasswordLocators.SHOW_PASSWORD_BUTTON)
        self.click_element(RecoveryPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Найти активное поле Пароль')
    def find_input_active(self):
        self.wait_for_element(RecoveryPasswordLocators.INPUT_ACTIVE)
        return self.check_element_display(RecoveryPasswordLocators.INPUT_ACTIVE)