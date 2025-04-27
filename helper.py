from faker import Faker
import allure
import requests
from url import URLS


fake = Faker()
fakeRU = Faker(locale='ru_RU')


@allure.step("Генерация данных")
def generate_data():
    return {
        'name': fake.name(),
        'password': fake.password(length=10, special_chars=True, digits=True),
        'email': f"{fake.user_name()}@mail.ru"
    }

@allure.step("Создание email")
def create_user(user_data):
    response = requests.post(URLS.BASE_URL + URLS.CREATE_USER, json=user_data)
    return response

@allure.step("Удаление курьера в сервисе 'Самокат'")
def delete_user(user_id, access_token):
    headers = {'Authorization': access_token}
    response = requests.delete(URLS.BASE_URL + URLS.DELETE_USER + str(user_id), headers=headers)
    return response