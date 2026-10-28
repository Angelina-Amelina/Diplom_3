import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from urls import Urls
from helpers import generate_user_data


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    driver.maximize_window()
    driver.get(Urls.MAIN_PAGE)

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def user_api():
    data = generate_user_data()
    response = requests.post(Urls.API_REGISTER, json=data)
    assert response.status_code == 200, f"Не удалось зарегистрировать юзера: {response.text}"

    tokens = response.json()

    yield {
        "tokens": tokens,
        "user_data": data
    }

    auth_token = tokens.get("accessToken")
    if auth_token:
        requests.delete(Urls.API_USER, headers={"Authorization": auth_token})


@pytest.fixture(scope="function")
def authorized_user(driver, user_api):
    access_token = user_api['tokens']['accessToken']
    refresh_token = user_api['tokens']['refreshToken']

    driver.get(Urls.MAIN_PAGE)

    driver.execute_script(f"window.localStorage.setItem('accessToken', '{access_token}');")
    driver.execute_script(f"window.localStorage.setItem('refreshToken', '{refresh_token}');")

    driver.refresh()

    return user_api
