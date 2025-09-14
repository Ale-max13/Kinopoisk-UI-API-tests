import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Поиск")
def test_search_bar_is_displayed():
    with allure.step("Запуск браузера"):
        service = Service(executable_path="./yandexdriver.exe")
        options = webdriver.ChromeOptions()
        options.binary_location = config.YANDEX_BROWSER_PATH
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=service, options=options)

    with allure.step("Открываем сайт Кинопоиск"):
        driver.get("https://www.kinopoisk.ru/")

    with allure.step("Проверяем наличие строки поиска"):
        search_bar = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "kp_query"))
        )
        assert search_bar.is_displayed()

    driver.quit()


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Карточка фильма")
def test_movie_card_is_displayed():
    with allure.step("Запуск браузера"):
        service = Service(executable_path="./yandexdriver.exe")
        options = webdriver.ChromeOptions()
        options.binary_location = config.YANDEX_BROWSER_PATH
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=service, options=options)

    with allure.step("Открываем сайт Кинопоиск"):
        driver.get("https://www.kinopoisk.ru/")

    with allure.step("Вводим текст в поиск"):
        search_bar = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "kp_query"))
        )
        search_bar.send_keys("Оно\n")

    with allure.step("Проверяем наличие карточки фильма"):
        movie_card = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[href*="/film/"]')
            )
        )
        assert movie_card.is_displayed()

    driver.quit()


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Популярные фильмы")
def test_popular_movies_page():
    with allure.step("Запуск браузера"):
        service = Service(executable_path="./yandexdriver.exe")
        options = webdriver.ChromeOptions()
        options.binary_location = config.YANDEX_BROWSER_PATH
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=service, options=options)

    with allure.step("Открываем страницу популярных фильмов"):
        driver.get("https://www.kinopoisk.ru/lists/movies/popular/")

    with allure.step("Проверяем наличие карточки фильма"):
        movie_card = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[href*="/film/"]')
            )
        )
        assert movie_card.is_displayed()

    driver.quit()


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Главная страница")
def test_main_page_title():
    with allure.step("Запуск браузера"):
        service = Service(executable_path="./yandexdriver.exe")
        options = webdriver.ChromeOptions()
        options.binary_location = config.YANDEX_BROWSER_PATH
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=service, options=options)

    with allure.step("Открываем сайт Кинопоиск"):
        driver.get("https://www.kinopoisk.ru/")

    with allure.step("Проверяем заголовок страницы"):
        assert "Кинопоиск" in driver.title

    driver.quit()


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Кнопка входа")
def test_login_button_is_displayed():
    with allure.step("Запуск браузера"):
        service = Service(executable_path="./yandexdriver.exe")
        options = webdriver.ChromeOptions()
        options.binary_location = config.YANDEX_BROWSER_PATH
        options.add_argument("--disable-logging")
        options.add_argument("--log-level=3")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(service=service, options=options)

    with allure.step("Открываем сайт Кинопоиск"):
        driver.get("https://www.kinopoisk.ru/")

    with allure.step("Проверяем наличие кнопки 'Войти'"):
        login_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(text(),'Войти')]")
            )
        )
        assert login_button.is_displayed()

    driver.quit()
