import allure
from pages.header_page import HeaderPage
from pages.constructor_page import ConstructorPage


@allure.suite("Проверка основного функционала конструктора")
class TestConstructor:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor_button_navigates_to_main(self, driver):
        header_page = HeaderPage(driver)

        header_page.click_feed_button()
        header_page.click_constructor_button()

        assert header_page.is_constructor_section_active()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed_button_navigates_to_feed(self, driver):
        header_page = HeaderPage(driver)

        header_page.click_feed_button()

        assert "feed" in driver.current_url

    @allure.title("При клике на ингредиент появляется всплывающее окно с деталями")
    def test_click_ingredient_opens_modal(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.click_on_bun_ingredient()
        assert constructor_page.is_modal_details_window_displayed()

        constructor_page.click_close_modal_button()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_modal_via_cross_button(self, driver):
        constructor_page = ConstructorPage(driver)

        constructor_page.click_on_bun_ingredient()
        constructor_page.click_close_modal_button()

        assert constructor_page.is_modal_details_window_closed()

    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер")
    def test_drag_and_drop_ingredient_increases_counter(self, driver):
        constructor_page = ConstructorPage(driver)

        initial_count = constructor_page.get_bun_counter_value()
        constructor_page.drag_bun_to_cart()
        new_count = constructor_page.get_bun_counter_value()

        assert new_count > initial_count

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, driver, authorized_user):
        constructor_page = ConstructorPage(driver)

        constructor_page.drag_bun_to_cart()
        constructor_page.click_create_order_button()
        assert constructor_page.is_order_success_modal_displayed()

        constructor_page.click_close_modal_button()
