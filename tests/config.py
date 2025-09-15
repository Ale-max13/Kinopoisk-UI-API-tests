import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")
YANDEX_BROWSER_PATH = os.getenv("YANDEX_BROWSER_PATH", None)
CHROME_BROWSER_PATH = os.getenv("CHROME_BROWSER_PATH", None)

print("DEBUG BASE_URL:", BASE_URL)
print("DEBUG API_TOKEN:", API_TOKEN)
