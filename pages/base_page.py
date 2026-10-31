import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получение текущего URL браузера")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Поиск всех элементов по локатору: {locator}")
    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Скролл к элементу: {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_visibility(self, locator, timeout=20):
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

    @allure.step("Ожидание, пока текст элемента {locator} изменится и не будет равен {bad_texts}")
    def wait_for_text_to_change(self, locator, bad_texts=("", "9999"), timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).text.strip() not in bad_texts
        )

    @allure.step("Ожидание появления текста '{search_text}' в списке элементов: {locator}")
    def wait_for_text_in_elements_list(self, locator, search_text, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: any(search_text in el.text for el in d.find_elements(*locator))
        )

    @allure.step("Ожидание обновления URL-адреса")
    def wait_for_url_contains(self, url_part, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda d: url_part in d.current_url)

    @allure.step("Ожидание значения счётчика 'Выполнено за всё время': {expected_count}")
    def wait_until_condition(self, condition_func, timeout=15):
        return WebDriverWait(self.driver, timeout).until(lambda d: condition_func())

