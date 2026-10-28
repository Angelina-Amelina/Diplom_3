from selenium.webdriver.common.by import By


class ConstructorLocators:
    # Вкладки категорий ингредиентов
    BUN_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    # Карточка конкретного ингредиента (например, булки)
    BUN_INGREDIENT = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a")

    # Цифровой счетчик (каунтер) на карточке ингредиента
    BUN_COUNTER = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/preceding-sibling::div/p")

    # Зона корзины (куда перетаскивать ингредиенты)
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")

    # Кнопка "Оформить заказ"
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")


    # МОДАЛЬНЫЕ ОКНА
    # Открытое модальное окно
    MODAL_DETAILS_OPEN = (By.XPATH, "//*[contains(@class, 'Modal_modal_')]//h2[text()='Детали ингредиента']")
    # Кнопка-крестик для закрытия модального окна
    MODAL_CLOSE_BUTTON = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]")

    # Текст "Идентификатор заказа" внутри появившегося окна
    MODAL_ORDER_SUCCESS = (By.XPATH, "//p[text()='идентификатор заказа']")
    # Номер созданного заказа (цифры в центре экрана)
    ORDER_NUMBER = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']//h2")

    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
