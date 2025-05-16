import pytest
import allure


@allure.feature("Примеры тестов")
class TestExample:
    @allure.story("Простые проверки")
    @allure.title("Проверка равенства чисел")
    def test_numbers(self):
        with allure.step("Проверяем что 2+2 равно 4"):
            assert 2 + 2 == 4, "Ожидается, что 2+2 будет 4"

    @allure.story("Простые проверки")
    @allure.title("Проверка неравенства чисел")
    def test_numbers_failure(self):
        with allure.step("Проверяем что 2*2 не равно 5"):
            assert 2 * 2 != 5, "Ожидается, что 2*2 не будет 5"

    @allure.story("Проверки строк")
    @allure.title("Проверка содержания подстроки")
    def test_strings(self):
        with allure.step("Проверяем наличие подстроки"):
            assert "hello" in "hello world", "Ожидается, что 'hello' есть в строке"


@allure.feature("Параметризованные тесты")
class TestParametrized:
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (5, 5, 10),
        (10, -5, 5)
    ])
    @allure.story("Проверка сложения чисел")
    def test_addition(self, a, b, expected):
        with allure.step(f"Проверяем что {a} + {b} = {expected}"):
            assert a + b == expected, f"Ожидается, что {a}+{b} будет {expected}"