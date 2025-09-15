# 🎬 Kinopoisk-UI-API-tests

Автоматизация UI и API тестов для сайта [Кинопоиск](https://www.kinopoisk.ru/).

## 📦 Подготовка окружения
1. Установить зависимости:
```bash
pip install -r requirements.txt


2. Создать файл `.env` (см. `.env.example`) и указать:
```env
CHROME_BROWSER_PATH=<путь до chrome.exe>
BASE_URL=https://api.kinopoisk.dev/v1.4
API_TOKEN=<ваш API токен>

3. 🧰 Установка Allure CLI (Windows)
```powershell
choco install allure
allure --version

## 🚀 Запуск тестов:

```bash
# Все тесты
pytest -v

# Только UI
pytest -m ui -v

# Только API
pytest -m api -v

# UI + API вместе
pytest -m "ui or api" -v


## ✅ Покрытие тестами

### UI (5 тестов)
- ✅ Поиск
- ✅ Карточка фильма
- ✅ Популярные фильмы
- ✅ Заголовок страницы
- ✅ Кнопка «Войти»

### API (5 тестов)
- ✅ Поиск фильмов
- ✅ Поиск «Интерстеллар»
- ✅ Параметр limit=1
- ✅ Пустой query
- ✅ Неверный токен


⚠️ Известный нюанс:
При частых запусках UI тестов Кинопоиск может показывать капчу «Вы не робот?».  
Это защита ресурса, не ошибка тестов!


## 📊 Результаты тестов:
### Все тесты (UI + API) и Allure:

<img width="941" height="498" alt="UI_API_testing" src="https://github.com/user-attachments/assets/9e9c3e1f-860b-4a0c-8034-e52c41299af6" />
<img width="1918" height="735" alt="Allure" src="https://github.com/user-attachments/assets/10ffe5ee-875f-4f51-985a-423fb8ff9c9a" />


### ✅ Чек-лист перед запуском
- Установлен Google Chrome и подходящий chromedriver.exe в корне репозитория
- `.env` заполнен (CHROME_BROWSER_PATH, BASE_URL, API_TOKEN)
- Зависимости установлены: `pip install -r requirements.txt`
- Allure CLI установлен (choco/scoop)
