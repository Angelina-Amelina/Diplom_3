import allure
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


@allure.suite("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_click_profile_button_opens_account(self, driver,  authorized_user):
        header_page = HeaderPage(driver)

        header_page.click_profile_button()

        assert "account" in driver.current_url

    @allure.title("Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, driver,  authorized_user):
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)

        header_page.click_profile_button()
        login_page.click_order_history_sub_button()

        assert "account/order-history" in driver.current_url

    @allure.title("Выход из аккаунта")
    def test_logout_from_profile(self, driver,  authorized_user):
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)

        header_page.click_profile_button()
        login_page.click_logout_button()

        assert login_page.is_url_login()
