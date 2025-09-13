from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

    search_bar = driver.find_element(By.NAME, "kp_query")
    assert search_bar.is_displayed()
    driver.quit()
