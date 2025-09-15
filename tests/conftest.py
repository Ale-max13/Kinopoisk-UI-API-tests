import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import config

@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path="./chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.binary_location = config.CHROME_BROWSER_PATH
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(50)

    driver.get("https://www.kinopoisk.ru/")
    WebDriverWait(driver, 120).until(
        EC.any_of(
            EC.title_contains("Кинопоиск"),
            EC.title_contains("Вы не робот")
        )
    )
    if "Вы не робот" in driver.title:
        WebDriverWait(driver, 120).until(
            EC.any_of(
                EC.title_contains("Кинопоиск"),
                EC.presence_of_element_located((By.NAME, "kp_query"))
            )
        )

    yield driver
    driver.quit()
