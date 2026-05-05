from selenium.webdriver.common.by import By

class MainPageLocators:
    # Вопросы о важном- кнопки-вопросы (по порядку)
    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    
    # Вопросы о важном- текст ответов (по порядку)
    ANSWER_1 = (By.ID, "accordion__panel-0")
    ANSWER_2 = (By.ID, "accordion__panel-1")
    ANSWER_3 = (By.ID, "accordion__panel-2")
    ANSWER_4 = (By.ID, "accordion__panel-3")
    ANSWER_5 = (By.ID, "accordion__panel-4")
    ANSWER_6 = (By.ID, "accordion__panel-5")
    ANSWER_7 = (By.ID, "accordion__panel-6")
    ANSWER_8 = (By.ID, "accordion__panel-7")

    # кнопка согласия с куки при первом заходе
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button") 

    # Кнопка Заказать - хедер
    ORDER_BUTTON_TOP = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    #Кнопка Заказать - середина страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button")

    # Кнопка логотип Самокат
    LOGO_SCOOTER = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    # Кнопка логотип Яндекс
    LOGO_YANDEX = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
