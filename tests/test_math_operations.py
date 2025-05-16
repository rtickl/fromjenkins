import pytest
import allure
import math


@allure.feature("Математические операции")
class TestMathOperations:
    @allure.story("Операции с квадратным корнем")
    @allure.title("Проверка вычисления квадратного корня")
    def test_sqrt(self):
        with allure.step("Вычисляем квадратный корень из 16"):
            result = math.sqrt(16)
            with allure.step("Проверяем что результат равен 4"):
                assert result == 4, "Квадратный корень из 16 должен быть 4"

    @allure.story("Операции с факториалом")
    @allure.title("Проверка вычисления факториала")
    def test_factorial(self):
        with allure.step("Вычисляем факториал 5"):
            result = math.factorial(5)
            with allure.step("Проверяем что результат равен 120"):
                assert result == 120, "Факториал 5 должен быть 120"

    @allure.story("Тригонометрические функции")
    @allure.title("Проверка функции синуса")
    def test_sin(self):
        with allure.step("Вычисляем sin(π/2)"):
            result = math.sin(math.pi/2)
            with allure.step("Проверяем что результат ≈ 1"):
                assert abs(result - 1) < 1e-6, "sin(π/2) должен быть ≈ 1"