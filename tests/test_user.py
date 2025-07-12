import pytest
import requests

def test_authentication_failed(mocker):
    url = "https://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}

    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""

    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text.strip() == ""

def test_authentication_successful(mocker):
    url = "https://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""

    mocker.patch("requests.get", return_value=mock_response)

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text.strip() == ""