# test_dz_12_10_2023.py
"""
1. Разработать тесты (минимум три) в одном файле, оформить согласно правилам PyTest.
Можно завернуть его в тест-сьюит (в класс), можно отдельными методами (функциями).
Использовать при этом методы автостарта и автозакрытия браузера.
Использовать фикстуру по примеру классной работы.
Обязательно использовать хоть в одном из тестов проверку результата (assert).
тесты – произвольные. Можете взять сайт, можете математические какие-либо примеры/определения/утверждения.
Задействовать фикстуру с областью видимости (scope=class), а также фикстуру с автоиспользованием (autouse=True).

Задание представить в виде ссылки на репо в хите.
(Напоминаю, что у репо обязательно должен быть файл requirements.txt, readme файл, и Ваш файл с кодом скрипта,
больше ничего не должно быть, никаких директорий с Вашим виртуальным окружением, никаких лишних файлов).
Привыкаем оформлять свои проекты правильно.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://solmar.com.ua/ua/"

"""
Якщо активуємо цей код, то область видимості буде в рамках класу, і тоді браузер відкриється і закриється лише один раз, 
а всі тести будуть виконуватись один за одним, в одному й тому ж екземплярі браузера. Так робити НЕ рекомендується.
"""
# @pytest.fixture(scope="class")
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

"""Автовикористання фікстур"""
@pytest.fixture(autouse=True)
def prepare_data():
    print("print this str for every test")

class TestDz_12_10_2023_1():
    # викликаємо фікстуру в тесті, передавши її як параметр
    def test_math_1(self, browser):
        browser.get(link)
        result = 3 ** 2  # Возводим 5 в квадрат
        expected_result = 9
        assert result == expected_result

    def test_math_2(self, browser):
        browser.get(link)
        result = 10 ** 2  # Возводим 5 в квадрат
        expected_result = 100
        assert result == expected_result

    def test_math_3(self, browser):
        browser.get(link)
        num1 = 10
        num2 = 5
        result = num1 + num2
        expected_result = 15
        assert result == expected_result

