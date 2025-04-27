import allure
import pytest
from selenium import webdriver
from url import URLS
import helper


@allure.step('Открытие браузера')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
       chrome_options = webdriver.ChromeOptions()
       driver = webdriver.Chrome(options=chrome_options)

    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)

    driver.maximize_window()
    driver.get(URLS.BASE_URL)
    yield driver

    driver.quit()


@pytest.fixture
def create_user_data():
    user_data = helper.generate_data()
    response = helper.create_user(user_data)
    user_id = response.json().get('user', {}).get('id')
    access_token = response.json().get('accessToken')
    yield user_data, access_token

    if user_id:
        helper.delete_user(user_id, access_token)
