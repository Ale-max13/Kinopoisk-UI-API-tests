import pytest
import requests
import config
import allure


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_movie_by_title():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": config.API_TOKEN}
    params = {"query": "Оно"}

    with allure.step("Отправляем запрос на поиск фильма по названию"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем статус-код и наличие результатов"):
        assert response.status_code == 200
        assert len(response.json().get("docs", [])) > 0


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_movie_interstellar():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": config.API_TOKEN}
    params = {"query": "Интерстеллар"}

    with allure.step("Отправляем запрос на поиск фильма 'Интерстеллар'"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем статус-код и наличие результатов"):
        assert response.status_code == 200
        assert len(response.json().get("docs", [])) > 0


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_with_limit():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": config.API_TOKEN}
    params = {"query": "Оно", "limit": 1}

    with allure.step("Отправляем запрос с параметром limit=1"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем статус-код и количество результатов"):
        assert response.status_code == 200
        assert len(response.json().get("docs", [])) == 1


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_empty_query():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": config.API_TOKEN}
    params = {"query": ""}

    with allure.step("Отправляем запрос с пустым query"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем статус-код (ожидаем 200)"):
        assert response.status_code == 200
    

@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_with_invalid_token():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": "12345"}
    params = {"query": "Оно"}

    with allure.step("Отправляем запрос с неверным токеном"):
        response = requests.get(url, headers=headers, params=params)

    with allure.step("Проверяем, что возвращается 401 Unauthorized"):
        assert response.status_code == 401
