from selenium.webdriver.common.by import By


class HeaderLocators:
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]/parent::a")
    # Кнопка "Лента Заказов"
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]/parent::a")
    # Кнопка "Личный Кабинет"
    PROFILE_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]/parent::a")
    # Логотип Stellar Burgers по центру
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
