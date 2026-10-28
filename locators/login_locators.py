from selenium.webdriver.common.by import By


class LoginLocators:
    # Поля ввода на странице Login
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылки для переходов
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")

    # СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ
    FORGOT_EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # СТРАНИЦА СБРОСА ПАРОЛЯ
    # Иконка "глаза" (кнопка показать/скрыть пароль)
    PASSWORD_EYE_ICON = (By.CSS_SELECTOR, ".input__icon")
    # Контейнер инпута пароля
    PASSWORD_INPUT_CONTAINER = (By.XPATH, "//label[text()='Пароль']/parent::div")

    # СТРАНИЦА ЛИЧНОГО КАБИНЕТА
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
