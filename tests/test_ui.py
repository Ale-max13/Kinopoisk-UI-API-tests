from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_bar_is_displayed():
    service = Service(executable_path="./yandexdriver.exe")
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Users\alena\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.kinopoisk.ru/")

    search_bar = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "kp_query"))
    )
    assert search_bar.is_displayed()
    driver.quit()


def test_movie_card_is_displayed():
    service = Service(executable_path="./yandexdriver.exe")
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Users\alena\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.kinopoisk.ru/")

    search_bar = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "kp_query"))
    )
    search_bar.send_keys("Оно\n")

    movie_card = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/film/"]'))
    )
    assert movie_card.is_displayed()
    driver.quit()


def test_popular_movies_page():
    service = Service(executable_path="./yandexdriver.exe")
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Users\alena\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.kinopoisk.ru/lists/movies/popular/")

    movie_card = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/film/"]'))
    )
    assert movie_card.is_displayed()
    driver.quit()