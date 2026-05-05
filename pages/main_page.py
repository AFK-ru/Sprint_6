from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls
import allure

class MainPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.driver.get(Urls.MAIN_PAGE_URL)

    @allure.step("Принятие куки")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Получение текста ответа на вопрос")
    def get_answer(self, q_locator, a_locator):
        self.scroll_to(q_locator)
        self.click(q_locator)
        return self.find_element(a_locator).text
    
    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)
