import allure

from locator import *
from page.base_page import BasePage
from helper import *
from selenium.webdriver.support.ui import WebDriverWait

class OrderPage(BasePage):
    @allure.step('Нажимаем на заказ в списке Лента заказов')
    def click_order(self):
        self.click_element(OrdersFeedPageLocators.ORDER_LINK)

    @allure.step('Получаем текста заголовка конструктора')
    def get_text_on_title_of_feed(self):
        self.wait_for_element(OrdersFeedPageLocators.ORDERS_LIST_TITLE)
        return self.get_element_text(OrdersFeedPageLocators.ORDERS_LIST_TITLE)

    @allure.step("Проверяем открытие окна с деталями заказа")
    def check_open_window_with_order_details(self):
        return self.check_element_display(OrdersFeedPageLocators.ORDER_COMPOUND)

    @allure.step("Получаем номер последнего заказа")
    def get_order_number(self):
        self.wait_for_element(OrdersFeedPageLocators.ALL_ORDERS_IN_ACC)
        number_last=self.find_element(OrdersFeedPageLocators.ALL_ORDERS_IN_ACC)
        return number_last.text

    @allure.step("Получаем количество заказов на странице 'Лента заказов'")
    def get_orders_counter(self):
        self.wait_for_element(OrdersFeedPageLocators.ALL_ORDERS_AT_FEED)
        number_all = self.find_element(OrdersFeedPageLocators.ALL_ORDERS_AT_FEED)
        return number_all.text

    @allure.step("Получаем количество заказов выполненных за все время ")
    def get_orders_counter_all_time(self):
        self.wait_for_element(OrdersFeedPageLocators.ALL_ORDER_COUNT)
        number_today = self.find_element(OrdersFeedPageLocators.ALL_ORDER_COUNT)
        return int(number_today.text)

    @allure.step("Получаем значение счётчика 'Выполнено за сегодня' ")
    def get_orders_counter_today(self):
        self.wait_for_element(OrdersFeedPageLocators.DAILY_ORDER_COUNT)
        number_today = self.find_element(OrdersFeedPageLocators.DAILY_ORDER_COUNT)
        return int(number_today.text)

    @allure.step("Получаем номер заказа в разделе 'В работе'")
    def get_order_in_works_number(self):
        self.wait_for_element(OrdersFeedPageLocators.NUMBER_IN_PROGRESS)
        number_work = self.find_element(OrdersFeedPageLocators.NUMBER_IN_PROGRESS)
        return int(number_work.text)

    @allure.step("Проверяем открытие окна с деталями заказа")
    def check_open_window_with_order_details(self):
        return self.check_element_display(OrdersFeedPageLocators.INGREDIENT_IN_ORDER)

    @allure.step("Получить Email для авторизации из сгенерированных данных")
    def get_user_email(self, user_response):
        email = user_response["email"]
        return email

    @allure.step("Получить Password для авторизации из сгенерированных данных")
    def get_user_password(self, user_response):
        password = user_response["password"]
        return password

    @allure.step("Вводим email в поле email")
    def set_email(self, email):
        input_email = self.find_element(PersonalAccLocators.EMAIL_FIELD)
        input_email.clear()
        input_email.send_keys(email)

    @allure.step("Вводим password в поле 'password'")
    def set_password(self, password):
        input_password = self.find_element(PersonalAccLocators.PASSWORD_FIELD)
        input_password.clear()
        input_password.send_keys(password)

    @allure.step('Получаем номер заказа')
    def fetch_order_id(self):
        self.wait_for_element(MainPageLocators.ORDER_IDENTIFICATE)

        # Ждем, пока текст элемента не станет отличаться от '9999'
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_element_text(MainPageLocators.ORDER_NUMBER) != '9999'
        )

        order_id = self.get_element_text(MainPageLocators.ORDER_NUMBER)
        return int(order_id)

