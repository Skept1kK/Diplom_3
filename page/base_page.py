import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Ждем загрузку элемента')
    def wait_for_element(self, locator, visibility=True, timeout=10):
        condition = (EC.visibility_of_element_located if visibility
                     else EC.presence_of_element_located)
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        time.sleep(1)
        self.find_element(locator).click()

    @allure.step('Вводим данные в поле')
    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step('Дожидаемся кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    @allure.step('Проверить отображение элемента')
    def check_element_display(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Захватываем и переносим элемент')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)
        action_chains = ActionChains(self.driver)
        action_chains.click_and_hold(source_element).move_to_element(target_element).release().pause(5).perform()

    @allure.step('получаем текст элемента')
    def get_element_text(self, locator, use_text_content=False):
        self.wait_for_element(locator)
        element = self.driver.find_element(*locator)

        if use_text_content:
            return element.get_attribute('textContent').strip()
        else:
            return element.text.strip()