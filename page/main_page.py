import allure

from locator import *
from page.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    @allure.step('Переход на страницу конструктора')
    def click_on_constructor(self):
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_feed_button(self):
        self.wait_for_element(MainPageLocators.BUTTON_ORDERS_LIST)
        self.click_element(MainPageLocators.BUTTON_ORDERS_LIST)

    @allure.step('Получение заголовка страницы')
    def get_text_on_title(self):
        return self.get_element_text(MainPageLocators.TITLE_OF_MAIN)

    @allure.step('Кликнуть по ингредиенту')
    def click_on_ingredient(self):
        self.wait_for_element(MainPageLocators.BURGER_INGREDIENT)
        self.click_element(MainPageLocators.BURGER_INGREDIENT)

    @allure.step('Проверить отображение окна "Детали ингредиента"')
    def check_displaying_window_details(self):
        self.wait_for_element(MainPageLocators.DETAILS_INGREDIENT)
        return self.check_element_display(MainPageLocators.DETAILS_INGREDIENT)

    @allure.step('Проверить отображение окна "Детали заказа"')
    def check_displaying_details_of_order(self):
        self.wait_for_element(MainPageLocators.ORDER_NOTIFICATION)
        return self.check_element_display(MainPageLocators.ORDER_NOTIFICATION)


    @allure.step('Закрыть окно')
    def close_window(self):
        self.wait_for_element(MainPageLocators.CLOSE_WINDOW)

        # Ждем, пока текст элемента не станет отличаться от '9999'
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_element_text(MainPageLocators.ORDER_NUMBER) != '9999'
        )

        self.click_element(MainPageLocators.CLOSE_WINDOW)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной странице сайта')
    def click_on_button_login(self):
        self.click_element(PersonalAccLocators.PERSONAL_ACCOUNT_BUTTON)


    @allure.step('Добавить ингредиент')
    def add_filling_to_order(self):
        self.find_element(MainPageLocators.BURGER_INGREDIENT)
        self.drag_and_drop_element(MainPageLocators.BURGER_INGREDIENT, MainPageLocators.PLACE_FOR_ORDER)

    @allure.step('Получить количество ингредиентов')
    def get_count_of_ingredients(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Кликнуть на кнопку создания заказа')
    def click_on_button_make_order(self):
        self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)


    @allure.step('Кликнуть на кнопку закрытия окна о создании заказа')
    def click_on_button_close(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.CLOSE_WINDOW)
        self.click_element(MainPageLocators.CLOSE_WINDOW)




