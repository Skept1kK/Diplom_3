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

    #@allure.step('Заполняем поле "Имя"')
    #def set_name_field(self, user_name):
        #self.click_element(PersonalAccLocators.USER_NAME_INPUT)
        #self.set_value(PersonalAccLocators.USER_NAME_INPUT, user_name)

    @allure.step('Ждем загрузки кнопки "Зарегистрироваться"')
    def wait_visibility_of_button_register(self):
        self.wait_for_element(PersonalAccLocators.REG_BUTTON)
        self.check_element_display(PersonalAccLocators.REG_BUTTON)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.click_element(PersonalAccLocators.LOGIN_BUTTON)

    @allure.step('Кликаем на кнопку "История заказов"')
    def click_on_order_history_button(self):
        self.click_element(PersonalAccLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Проверяем отображение кнопки "История заказов"')
    def check_on_order_history_button(self):
        self.wait_for_element(PersonalAccLocators.ORDER_HISTORY_BUTTON)
        self.check_element_display(PersonalAccLocators.ORDER_HISTORY_BUTTON)

    #@allure.step("Получить номер последнего заказа")
    #def get_order_number_history(self):
        #self.wait_for_element(PersonalAccLocators.CARD_ORDER)
        #number = self.find_element(PersonalAccLocators.CARD_ORDER)
        #return int(number.text)

    @allure.step('Проверяем активацию кнопки "История заказов"')
    def check_on_order_history(self):
        self.wait_for_element(PersonalAccLocators.ACTIV_HISTORY_BUTTON,PersonalAccLocators.CARD_ORDER)
        self.check_element_display(PersonalAccLocators.ACTIV_HISTORY_BUTTON,PersonalAccLocators.CARD_ORDER)


    @allure.step('Кликаем на кнопку "Выйти"')
    def click_on_logout_button(self):
        self.click_element(PersonalAccLocators.LOGOUT_BUTTON)

