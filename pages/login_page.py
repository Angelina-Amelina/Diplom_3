import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    @allure.step("Авторизация пользователя: {email}")
    def login(self, email, password):
        self.input_text(LoginLocators.EMAIL_INPUT, email)
        self.input_text(LoginLocators.PASSWORD_INPUT, password)
        self.click_element(LoginLocators.ENTER_BUTTON)

    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click_element(LoginLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Ввод почты {email} на странице восстановления")
    def enter_restore_email(self, email):
        self.input_text(LoginLocators.FORGOT_EMAIL_INPUT, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.click_element(LoginLocators.RESTORE_BUTTON)

    @allure.step("Клик по иконке показа/скрытия пароля (глаз)")
    def click_show_password_icon(self):
        self.click_element(LoginLocators.PASSWORD_EYE_ICON)

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        container = self.wait_for_visibility(LoginLocators.PASSWORD_INPUT_CONTAINER)
        return "input_status_active" in container.get_attribute("class")

    @allure.step("Переход в раздел 'История заказов'")
    def click_order_history_sub_button(self):
        self.click_element(LoginLocators.ORDER_HISTORY_LINK)

    @allure.step("Клик по кнопке 'Выход' в профиле")
    def click_logout_button(self):
        self.click_element(LoginLocators.LOGOUT_BUTTON)

    @allure.step("Проверка, что текущий URL соответствует странице логина")
    def is_url_login(self):
        WebDriverWait(self.driver, 5).until(lambda d: "login" in d.current_url)
        return True

    @allure.step("Ожидание перехода на страницу сброса пароля (reset-password)")
    def is_url_reset_password(self):
        from selenium.webdriver.support.wait import WebDriverWait
        WebDriverWait(self.driver, 10).until(lambda d: "reset-password" in d.current_url)
        return "reset-password" in self.driver.current_url
