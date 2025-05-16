import pytest
import allure
import requests


@allure.feature("Тесты веб-приложения")
class TestWebApp:
    API_URL = "https://jsonplaceholder.typicode.com"

    @allure.story("Проверка API")
    @allure.title("Получение списка пользователей")
    def test_get_users(self):
        with allure.step("Отправляем GET запрос к /users"):
            response = requests.get(f"{self.API_URL}/users")
            with allure.step("Проверяем код ответа"):
                assert response.status_code == 200, "Ожидается код ответа 200"
            with allure.step("Проверяем что ответ содержит данные"):
                assert len(response.json()) > 0, "Ожидается непустой список пользователей"

    @allure.story("Проверка API")
    @allure.title("Создание нового поста")
    def test_create_post(self):
        test_data = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        with allure.step("Отправляем POST запрос к /posts"):
            response = requests.post(
                f"{self.API_URL}/posts",
                json=test_data
            )
            with allure.step("Проверяем код ответа"):
                assert response.status_code == 201, "Ожидается код ответа 201"
            with allure.step("Проверяем данные в ответе"):
                response_data = response.json()
                assert response_data["title"] == test_data["title"], "Заголовок должен совпадать"
                assert response_data["body"] == test_data["body"], "Тело должно совпадать"