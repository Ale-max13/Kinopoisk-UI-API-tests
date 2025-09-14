import os
from dotenv import load_dotenv

load_dotenv()

YANDEX_BROWSER_PATH = os.getenv("YANDEX_BROWSER_PATH")
BASE_URL = os.getenv("BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")
