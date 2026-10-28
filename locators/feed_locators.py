from selenium.webdriver.common.by import By


class FeedLocators:
    # Первая ссылка-карточка заказа именно на странице «Лента заказов»
    FIRST_ORDER_CARD = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_list')]/li/a)[1]")
    # Модальное окно деталей заказа (универсальный локатор для открытой модалки)
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'opened')] | //div[contains(@class, 'Modal_orderBox')] | //section[contains(@class, 'opened')]")
    # Шаблон для поиска карточки с конкретным номером заказа в ленте
    ORDER_NUMBER_TEMPLATE = "//div[contains(@class, 'OrderFeed_orderId') and text()='#{order_id}']"

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")

    # Список номеров строго в блоке "В работе:" (заказы, которые готовятся)
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul[contains(@class, 'OrderFeed_orderList')]/li")
    # Заголовок страницы
    FEED_ORDER_NUMBERS_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    # Заказы в работе
    ORDER_NUMBERS = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li")