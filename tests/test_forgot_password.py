import allure
from urls import Urls
from pages.header_page import HeaderPage
from pages.login_page import LoginPage


@allure.suite("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigation_to_forgot_password_page(self, driver):
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)

        header_page.click_profile_button()
        login_page.click_forgot_password_link()

        assert Urls.FORGOT_PASSWORD_PAGE in driver.current_url

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_restore(self, driver):
        login_page = LoginPage(driver)
        driver.get(Urls.FORGOT_PASSWORD_PAGE)

        login_page.enter_restore_email("test_praktikum_ui@yandex.ru")
        login_page.click_restore_button()

        assert login_page.is_url_reset_password()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_eye_icon_highlights_password_field(self, driver):
        login_page = LoginPage(driver)
        driver.get(Urls.FORGOT_PASSWORD_PAGE)

        login_page.enter_restore_email("test_praktikum_ui@yandex.ru")
        login_page.click_restore_button()
        login_page.is_url_reset_password()
        login_page.click_show_password_icon()

        assert login_page.is_password_field_active()
