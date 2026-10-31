import allure
from seletools.actions import drag_and_drop
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators


class ConstructorPage(BasePage):
    @allure.step("Клик на ингредиент (булку)")
    def click_on_bun_ingredient(self):
        self.click_element(ConstructorLocators.BUN_INGREDIENT)

    @allure.step("Проверка отображения модального окна деталей")
    def is_modal_details_window_displayed(self):
        return self.wait_for_visibility(ConstructorLocators.MODAL_DETAILS_OPEN).is_displayed()

    @allure.step("Клик по крестику закрытия модального окна")
    def click_close_modal_button(self):
        self.click_element(ConstructorLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверка закрытия модального окна")
    def is_modal_details_window_closed(self):
        try:
            self.wait_for_invisibility(ConstructorLocators.MODAL_DETAILS_OPEN, timeout=10)
            return True
        except Exception:
            return False

    @allure.step("Получение значения каунтера ингредиента")
    def get_bun_counter_value(self):
        text = self.get_element_text(ConstructorLocators.BUN_COUNTER)
        return int(text) if text and text.isdigit() else 0

    @allure.step("Перетаскивание булки в корзину (Drag & Drop)")
    def drag_bun_to_cart(self):
        source_element = self.wait_for_visibility(ConstructorLocators.BUN_INGREDIENT)
        target_element = self.wait_for_visibility(ConstructorLocators.BURGER_CONSTRUCTOR_BASKET)

        drag_and_drop(self.driver, source_element, target_element)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_create_order_button(self):
        self.click_element(ConstructorLocators.CREATE_ORDER_BUTTON)

    @allure.step("Проверка появления модального окна успешного заказа")
    def is_order_success_modal_displayed(self):
        return self.wait_for_visibility(ConstructorLocators.MODAL_ORDER_SUCCESS).is_displayed()

    @allure.step("Ожидание появления номера заказа в модальном окне")
    def wait_order_number(self, timeout=15):
        element = self.wait_for_visibility(ConstructorLocators.ORDER_NUMBER, timeout)
        self.wait_for_text_to_change(ConstructorLocators.ORDER_NUMBER, bad_texts=("", "9999"), timeout=timeout)
        return element.text.strip()
