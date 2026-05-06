from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls
import allure

class MainPage(BasePage):

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        self.open_url(Urls.MAIN_PAGE_URL)

    @allure.step("Принятие куки")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)
    
    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Получение текста ответа на вопрос номер {index}")
    def get_answer_text(self, index):
        method, locator_string = MainPageLocators.QUESTION_LOCATOR
        q_locator = (method, locator_string.format(index))
        
        method_a, locator_string_a = MainPageLocators.ANSWER_LOCATOR
        a_locator = (method_a, locator_string_a.format(index))
        
        self.scroll_to(q_locator)
        self.click(q_locator)
        return self.find_element(a_locator).text

    @allure.step("Клик по кнопке 'Заказать' ({location})")
    def click_order_button(self, location):
        if location == "top":
            self.click(MainPageLocators.ORDER_BUTTON_TOP)
        else:
            self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)
