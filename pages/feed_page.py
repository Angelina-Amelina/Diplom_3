import allure
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators


class FeedPage(BasePage):
    @allure.step("Клик по первой карточке заказа в ленте")
    def click_first_order_in_feed(self):
        self.click_element(FeedLocators.FIRST_ORDER_CARD)

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
        clean_order_number = str(order_number).zfill(5)

        try:
            self.wait_for_text_in_elements_list(FeedLocators.ORDER_NUMBERS, clean_order_number, timeout=timeout)
            return True
        except Exception:
            return False

    @allure.step("Проверка наличия номера заказа в списке 'В работе'")
    def is_order_in_progress_list(self, order_number):
        self.wait_for_visibility(FeedLocators.ORDERS_IN_PROGRESS_LIST)
        elements = self.find_all_elements(FeedLocators.ORDERS_IN_PROGRESS_LIST)
        return any(order_number in el.text for el in elements)
