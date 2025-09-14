# 🎬 Kinopoisk-UI-API-tests

Автоматизация UI и API тестов для сайта [Кинопоиск](https://www.kinopoisk.ru/).

## 📦 Подготовка окружения
1. Установить зависимости:  
`pip install -r requirements.txt`  

2. Создать файл `.env` (см. `.env.example`) и указать:  
YANDEX_BROWSER_PATH=<путь до YandexBrowser.exe>
BASE_URL=https://api.kinopoisk.dev/v1.4
API_TOKEN=<ваш API токен>

## ▶️ Запуск тестов:
# Все тесты:
pytest -v
# Только UI:
pytest -m ui -v
# Только API:
pytest -m api -v

## 📊 Allure отчёт
# Сформировать результаты:
pytest -v --alluredir=allure-results
# Открыть отчёт:
allure serve allure-results

## ✅ Покрытие тестами
- UI (5 тестов):
Поиск
Карточка фильма
Популярные фильмы
Заголовок страницы
Кнопка «Войти»

- API (5 тестов):
Поиск фильмов
Поиск «Интерстеллар»
Параметр limit=1
Пустой query
Неверный токен

⚠️ Ограничения
При частых запусках UI тестов Кинопоиск может показывать капчу «Вы не робот?».
- Это защита ресурса, не ошибка тестов!