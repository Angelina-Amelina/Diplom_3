import allure
from pages.header_page import HeaderPage
from pages.feed_page import FeedPage
from pages.constructor_page import ConstructorPage


@allure.suite("Раздел «Лента заказов»")
class TestOrderFeed:

    @allure.title("При клике на заказ в ленте откроется всплывающее окно с деталями")
    def test_click_order_opens_modal_details(self, driver):
        header_page = HeaderPage(driver)
        feed_page = FeedPage(driver)

        header_page.click_feed_button()
        feed_page.click_first_order_in_feed()

        assert feed_page.is_order_modal_displayed()

    @allure.title("Заказы пользователя из «История заказов» отображаются на странице «Лента заказов»")
    def test_user_order_history_feed(self, driver, authorized_user):
        header_page = HeaderPage(driver)
        feed_page = FeedPage(driver)
        constructor_page = ConstructorPage(driver)

        header_page.click_constructor_button()
        constructor_page.drag_bun_to_cart()
        constructor_page.click_create_order_button()
        order_number = constructor_page.wait_order_number()
        constructor_page.click_close_modal_button()

        header_page.click_feed_button()
        assert feed_page.is_order_in_feed_list(order_number)

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_orders_counter_increases(self, driver, authorized_user):
        header_page = HeaderPage(driver)
        feed_page = FeedPage(driver)
        constructor_page = ConstructorPage(driver)

        header_page.click_feed_button()
        before = feed_page.get_total_orders_count()

        header_page.click_constructor_button()
        constructor_page.drag_bun_to_cart()
        constructor_page.click_create_order_button()
        constructor_page.wait_order_number()
        constructor_page.click_close_modal_button()

        header_page.click_feed_button()
        assert feed_page.wait_total_orders_count(before + 1)

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increases(self, driver, authorized_user):
        header_page = HeaderPage(driver)
        feed_page = FeedPage(driver)
        constructor_page = ConstructorPage(driver)

        header_page.click_feed_button()
        before = feed_page.get_today_orders_count()

        header_page.click_constructor_button()
        constructor_page.drag_bun_to_cart()
        constructor_page.click_create_order_button()
        constructor_page.wait_order_number()
        constructor_page.click_close_modal_button()

        header_page.click_feed_button()
        after = feed_page.get_today_orders_count()

        assert after == before + 1

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_new_order_appears_in_progress_section(self, driver, authorized_user):
        header_page = HeaderPage(driver)
        feed_page = FeedPage(driver)
        constructor_page = ConstructorPage(driver)

        header_page.click_constructor_button()
        constructor_page.drag_bun_to_cart()
        constructor_page.click_create_order_button()
        order_number = constructor_page.wait_order_number()
        constructor_page.click_close_modal_button()

        header_page.click_feed_button()
        assert feed_page.is_order_in_progress_list(order_number)
