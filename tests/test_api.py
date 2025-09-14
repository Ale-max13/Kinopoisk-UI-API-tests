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

    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 200
    assert len(response.json().get("docs", [])) > 0


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_movie_interstellar():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": config.API_TOKEN}
    params = {"query": "Интерстеллар"}

    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 200
    assert len(response.json().get("docs", [])) > 0


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_with_limit():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": config.API_TOKEN}
    params = {"query": "Оно", "limit": 1}

    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 200
    assert len(response.json().get("docs", [])) == 1


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_empty_query():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": config.API_TOKEN}
    params = {"query": ""}

    response = requests.get(url, headers=headers, params=params)

    assert response.status_code in [200, 400]


@pytest.mark.api
@allure.feature("API: Movie search")
def test_search_with_invalid_token():
    url = f"{config.BASE_URL}/movie/search"
    headers = {"X-API-KEY": "12345"}
    params = {"query": "Оно"}

    response = requests.get(url, headers=headers, params=params)

    assert response.status_code == 401
