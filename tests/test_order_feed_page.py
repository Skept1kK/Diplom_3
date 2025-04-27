import allure
from page.main_page import MainPage
from page.order_feed_page import OrderPage
from page.personal_account_page import AccountPage


class TestFeedPage:

    @allure.title('Проверка появления всплывающего окна с деталями заказа')
    def test_window_order_details(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)
        main_page.click_feed_button()
        order_feed_page.click_order()
        assert order_feed_page.check_open_window_with_order_details()



    @allure.title('Проверка отображения заказов из раздела «История заказов» на странице «Лента заказов»')
    def test_order_in_history_order(self, driver, create_user_data):
        user_data, access_token = create_user_data  # Получаем данные пользователя из фикстуры
        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)
        personal_account_page = AccountPage(driver)

        email = order_feed_page.get_user_email(user_data)
        password = order_feed_page.get_user_password(user_data)

        personal_account_page.click_on_personal_account_button()
        order_feed_page.set_email(email)
        order_feed_page.set_password(password)
        personal_account_page.click_login_button()

        main_page.add_filling_to_order()
        main_page.click_on_button_make_order()
        main_page.close_window()

        personal_account_page.click_on_personal_account_button()
        personal_account_page.click_on_order_history_button()
        order_number_history = order_feed_page.get_order_number()
        main_page.click_feed_button()
        order_feed_page.click_order()
        order_feed_page.check_open_window_with_order_details()
        order_number_feed = order_feed_page.get_orders_counter()

        assert order_number_history == order_number_feed

    @allure.title('Проверка счетчика заказов "Выполнено за все время"')
    def test_order_counter_all_time(self, driver, create_user_data):
        user_data, access_token = create_user_data  # Получаем данные пользователя из фикстуры
        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)
        personal_account_page = AccountPage(driver)

        email = order_feed_page.get_user_email(user_data)  # Получаем email
        password = order_feed_page.get_user_password(user_data)  # Получаем пароль

        main_page.click_feed_button()
        order_number_feed_old = order_feed_page.get_orders_counter_all_time()
        personal_account_page.click_on_personal_account_button()
        order_feed_page.set_email(email)
        order_feed_page.set_password(password)
        personal_account_page.click_login_button()

        main_page.add_filling_to_order()
        main_page.click_on_button_make_order()
        main_page.close_window()

        main_page.click_feed_button()
        order_number_feed_new = order_feed_page.get_orders_counter_all_time()

        assert order_number_feed_new == order_number_feed_old + 1, "Счетчик заказов увеличился на 1"

    @allure.title('Проверка счетчика заказов "Выполнено за сегодня"')
    def test_order_counter_today(self, driver, create_user_data):
        user_data, access_token = create_user_data  # Получаем данные пользователя из фикстуры
        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)
        personal_account_page = AccountPage(driver)

        email = order_feed_page.get_user_email(user_data)  # Получаем email
        password = order_feed_page.get_user_password(user_data)  # Получаем пароль

        main_page.click_feed_button()
        order_number_feed_old = order_feed_page.get_orders_counter_today()
        personal_account_page.click_on_personal_account_button()
        order_feed_page.set_email(email)
        order_feed_page.set_password(password)
        personal_account_page.click_login_button()

        main_page.add_filling_to_order()
        main_page.click_on_button_make_order()
        main_page.close_window()

        main_page.click_feed_button()
        order_number_feed_new = order_feed_page.get_orders_counter_today()

        assert order_number_feed_new == order_number_feed_old + 1, "Счетчик заказов увеличился на 1"

    @allure.title('Проверка счетчика заказов "Выполнено за сегодня"')
    def test_order_in_work(self, driver, create_user_data):
        user_data, access_token = create_user_data  # Получаем данные пользователя из фикстуры
        main_page = MainPage(driver)
        order_feed_page = OrderPage(driver)
        personal_account_page = AccountPage(driver)

        email = order_feed_page.get_user_email(user_data)  # Получаем email
        password = order_feed_page.get_user_password(user_data)  # Получаем пароль

        personal_account_page.click_on_personal_account_button()
        order_feed_page.set_email(email)
        order_feed_page.set_password(password)
        personal_account_page.click_login_button()

        main_page.add_filling_to_order()
        main_page.click_on_button_make_order()
        order_number = order_feed_page.fetch_order_id()
        main_page.close_window()

        main_page.click_feed_button()
        order_number_work_new = order_feed_page.get_order_in_works_number()

        assert order_number == order_number_work_new


