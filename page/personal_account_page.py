import allure
from locator import PersonalAccLocators
from page.base_page import BasePage
from data import TestData



class AccountPage(BasePage):

    @allure.step('Кликаем по кнопке перехода в личный кабинет')
    def click_on_personal_account_button(self):
        self.wait_for_element(PersonalAccLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(PersonalAccLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Заполняем поле "email"')
    def set_email_field(self):
        self.wait_for_element_to_be_clickable(PersonalAccLocators.EMAIL_FIELD)
        self.click_element(PersonalAccLocators.EMAIL_FIELD)
        self.set_value(PersonalAccLocators.EMAIL_FIELD,TestData.LOGIN_NAME)

    @allure.step('Заполняем поле "Пароль"')
    def set_password_field(self):
        self.click_element(PersonalAccLocators.PASSWORD_FIELD)
        self.set_value(PersonalAccLocators.PASSWORD_FIELD,TestData.USER_PASSWORD)


    @allure.step('Ждем загрузки и проверяем видимость кнопки "Зарегистрироваться"')
    def check_visibility_of_button_register(self):
        self.wait_for_element(PersonalAccLocators.REG_BUTTON)
        return self.check_element_display(PersonalAccLocators.REG_BUTTON)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.click_element(PersonalAccLocators.LOGIN_BUTTON)

    @allure.step('Кликаем на кнопку "История заказов"')
    def click_on_order_history_button(self):
        self.click_element(PersonalAccLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверяем отображение кнопки "История заказов"')
    def check_on_order_history_button(self):
        self.wait_for_element(PersonalAccLocators.ORDER_HISTORY_BUTTON)
        return self.check_element_display(PersonalAccLocators.ORDER_HISTORY_BUTTON)


    @allure.step('Проверяем активацию кнопки "История заказов"')
    def check_on_order_history(self):
        self.wait_for_element(PersonalAccLocators.CARD_ORDER)
        return self.check_element_display(PersonalAccLocators.CARD_ORDER)


    @allure.step('Кликаем на кнопку "Выйти"')
    def click_on_logout_button(self):
        self.click_element(PersonalAccLocators.LOGOUT_BUTTON)
