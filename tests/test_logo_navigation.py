from pages.main_page import MainPage
from urls import Urls
from locators.main_page_locators import MainPageLocators
import allure


@allure.title("Проверка навигации: клик на логотип 'Самокат' возвращает на главную страницу")
def test_click_scooter_logo_returns_to_main_page(driver):
    main_page = MainPage(driver)
    
    main_page.open_main_page()  #открытие главной страницы
    main_page.accept_cookies()  #подтверждение куки для избежания конфликта интерфейса
    
    main_page.click(MainPageLocators.ORDER_BUTTON_TOP)   #переход на страницу заказа
    
    main_page.click_scooter_logo()   #клик по логотипу Самокат
    
    assert main_page.get_current_url() == Urls.MAIN_PAGE_URL   #проверка совпадения url с главной страницей
