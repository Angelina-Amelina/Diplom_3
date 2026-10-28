import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента: {locator}")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_for_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    @allure.step("Ожидание, пока оверлей модального окна исчезнет")
    def wait_for_overlay_to_disappear(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator):
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def input_text(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента: {locator}")
    def get_element_text(self, locator):
        return self.wait_for_visibility(locator).text
