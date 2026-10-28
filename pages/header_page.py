import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.constructor_locators import ConstructorLocators

class HeaderPage(BasePage):
    @allure.step("Клик по кнопке 'Конструктор' в хедере")
    def click_constructor_button(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента Заказов' в хедере")
    def click_feed_button(self):
        try:
            self.wait_for_overlay_to_disappear(ConstructorLocators.MODAL_OVERLAY)
        except:
            pass # Если оверлея и не было, просто идем дальше
        self.click_element(HeaderLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик по кнопке 'Личный Кабинет' в хедере")
    def click_profile_button(self):
        self.click_element(HeaderLocators.PROFILE_BUTTON)

    @allure.step("Проверка активности вкладки 'Конструктор'")
    def is_constructor_section_active(self):
        element = self.wait_for_visibility(HeaderLocators.CONSTRUCTOR_BUTTON)
        return "AppHeader_header__link_active" in element.get_attribute("class")
