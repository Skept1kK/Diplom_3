from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')
    TITLE_OF_MAIN = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUTTON_ORDERS_LIST = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')
    BURGER_INGREDIENT = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')
    DETAILS_INGREDIENT = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')
    CLOSE_WINDOW = (By.XPATH, '//section[contains(@class, ''"Modal_modal_opened")]//button[contains(@class, "close")]')
    INGREDIENT_COUNTER = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[''@class="counter_counter__num__3nue1"][1]')
    PLACE_FOR_ORDER = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_IDENTIFICATE = (By.XPATH, '//p[text()="идентификатор заказа"]')
    ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    ORDER_NOTIFICATION = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    CLOSE_MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")'']//button[contains(@class, "close")]')


class PersonalAccLocators:

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    USER_NAME_INPUT = (By.XPATH, "(.//input[@name='name'])[1]")
    REG_BUTTON = (By.XPATH, '//a[text() = "Зарегистрироваться"]')
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href, "/forgot-password")]')
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    CARD_ORDER = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")


class RecoveryPasswordLocators:

    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    INPUT_ACTIVE = (By.CSS_SELECTOR, '.input.input_status_active')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class,"icon-action")]')
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')


class OrdersFeedPageLocators:

    INGREDIENT_IN_ORDER = (By.XPATH, "(//div[contains(@class,'Modal_imgBox__27yrH')])[1]")
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDER_COMPOUND = (By.XPATH, '//p[text()="Cостав"]')
    ORDER_LINK = (By.XPATH, '//*[contains(@class, "OrderHistory_link")]')
    ALL_ORDERS_IN_ACC = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, ""'text_type_digits-default')]")
    ALL_ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text ""text_type_digits-default']")
    ALL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem ""OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")