import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators


class FeedPage(BasePage):
    @allure.step("Клик по первой карточке заказа в ленте")
    def click_first_order_in_feed(self):
        element = self.wait_for_visibility(FeedLocators.FIRST_ORDER_CARD)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Проверка отображения окна с деталями заказа")
    def is_order_modal_displayed(self):
        return self.wait_for_visibility(FeedLocators.ORDER_DETAILS_MODAL).is_displayed()

    @allure.step("Получение значения счетчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        element = self.wait_for_visibility(FeedLocators.TOTAL_ORDERS_COUNTER)
        return int(element.text.strip())

    @allure.step("Ожидание значения счётчика 'Выполнено за всё время': {expected_count}")
    def wait_total_orders_count(self, expected_count, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_total_orders_count() == expected_count
        )

    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        element = self.wait_for_visibility(FeedLocators.TODAY_ORDERS_COUNTER)
        return int(element.text.strip())

    @allure.step("Проверка наличия номера заказа в общем списке ленты")
    def is_order_in_feed_list(self, order_number, timeout=15):
        self.wait_for_visibility(FeedLocators.FEED_ORDER_NUMBERS_HEADER)
        order_number = str(order_number).zfill(5)

        def order_is_in_list(driver):
            elements = driver.find_elements(*FeedLocators.ORDER_NUMBERS)
            order_texts = [element.text.strip() for element in elements]
            return order_number in order_texts

        return WebDriverWait(self.driver, timeout).until(order_is_in_list)

    @allure.step("Проверка наличия номера заказа в списке 'В работе'")
    def is_order_in_progress_list(self, order_number):
        self.wait_for_visibility(FeedLocators.ORDERS_IN_PROGRESS_LIST)
        elements = self.driver.find_elements(*FeedLocators.ORDERS_IN_PROGRESS_LIST)
        order_texts = [element.text for element in elements]
        order_number = str(order_number)
        return any(order_number in text for text in order_texts)
