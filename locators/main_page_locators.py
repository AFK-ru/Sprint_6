from selenium.webdriver.common.by import By

class MainPageLocators:
    
    QUESTION_LOCATOR = (By.ID, "accordion__heading-{}")
    ANSWER_LOCATOR = (By.ID, "accordion__panel-{}")
    
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
