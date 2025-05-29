import allure
from page.main_page import MainPage
from page.personal_account_page import AccountPage
from page.order_feed_page import OrderPage

class TestMainPage:

    @allure.title('Проверка перехода на страницу заказов')
    def test_switch_to_constructor(self, driver):
        main_page = MainPage(driver)
        personal_account_page=AccountPage(driver)
        personal_account_page.click_on_personal_account_button()
        main_page.click_on_constructor()
        assert 'Соберите бургер' in main_page.get_text_on_title()


    @allure.title('Проверка перехода на страницу "Лента заказов"')
    def test_switch_to_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)
        main_page.click_feed_button()
        assert 'Лента заказов' in order_feed_page.get_text_on_title_of_feed()


    @allure.title('Проверка появления окна "Детали ингредиента"')
    def test_window_details_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.check_displaying_window_details()


    @allure.title('Закрытие окна "Детали ингредиента" при клике на крестик')
    def test_closed_window_details_of_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.click_on_button_close()
        assert 'Соберите бургер' in main_page.get_text_on_title()


    @allure.title('Проверка счетчика заказов при добавлении ингредиента')
    def test_counter_for_ingredients_in_order(self, driver):
        main_page = MainPage(driver)
        main_page.add_filling_to_order()
        assert main_page.get_count_of_ingredients() == '2'


    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_making_order_authorized_user(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_login()
        personal_account_page = AccountPage(driver)
        personal_account_page.click_on_personal_account_button()
        personal_account_page.set_email_field()
        personal_account_page.set_password_field()
        personal_account_page.click_login_button()
        main_page.add_filling_to_order()
        main_page.click_on_button_make_order()
        assert main_page.check_displaying_details_of_order()


