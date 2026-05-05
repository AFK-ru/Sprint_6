from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Форма заказа №1
    NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")                                # Поле Имя
    SURNAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")                         # Поле Фамилия
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")      # Поле Адрес
    METRO_FIELD = (By.XPATH, ".//input[@placeholder='* Станция метро']")                     # Поле выбора станции метро
    METRO_STATION_ITEMS = (By.XPATH, "//div[contains(@class, 'select-search__option')]")     # Локатор для выбора станции
    PHONE_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")  # Поле Телефон
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")                                    # Кнопка Далее

    # Форма заказа №2
    DATE_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")                       # Поле выбора даты доставки
    RENT_TIME_FIELD = (By.CLASS_NAME, "Dropdown-control")                                              # Поле выбора срока аренды
    RENT_TIME_OPTIONS = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")                       # Локатор для выбора срока аренды
    COLOR_BLACK = (By.ID, "black")                                                                     # Выбор цвета самоката Черный
    COLOR_GREY = (By.ID, "grey")                                                                       # Выбор цвета самоката Серый
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")                     # Поле Коментарий для курьера
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")  # Кнопка Заказать

    # Подтверждение
    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")                                                            # Кнопка Да
    SUCCESS_HEADER = (By.XPATH, "//*[contains(text(), 'Заказ оформлен') or contains(@class, 'Order_ModalHeader')]")  # Заголовок окна успешного заказа
