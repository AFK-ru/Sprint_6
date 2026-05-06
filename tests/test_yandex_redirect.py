from pages.main_page import MainPage
from urls import Urls
import allure

class TestYandexRedirect:

    @allure.title("Проверка редиректа: клик на логотип Яндекса открывает страницу Дзена")
    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
    
        main_page.open_main_page()  #открытие главной страницы
        main_page.accept_cookies()  #подтверждение куки для избежания конфликта интерфейса
    
        main_page.click_yandex_logo()  #клик по логотипу Яндекс
    
        main_page.switch_to_new_tab()  #переключение на новую вкладку для дальнейшей проверки

        main_page.wait_for_url_contains(Urls.DZEN_URL)       #ожидание открытия страницы Дзен
        assert Urls.DZEN_URL in main_page.get_current_url()  #проверка совпадения url с главной страницей Дзен
