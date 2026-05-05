from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrderPage(BasePage):

    @allure.step("Заполнение первой формы: 'Для кого самокат'")
    def fill_first_form(self, name, surname, address, station, phone):
        self.find_element(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.find_element(OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        self.find_element(OrderPageLocators.ADDRESS_FIELD).send_keys(address)
        self.select_metro_station(station)
        self.find_element(OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбор станции метро: {station}")
    def select_metro_station(self, station):
        metro_input = self.find_element(OrderPageLocators.METRO_FIELD)
        metro_input.click()
        metro_input.send_keys(station)
        metro_input.send_keys(Keys.DOWN)
        metro_input.send_keys(Keys.ENTER)


    @allure.step("Выбор срока аренды: {duration}")
    def select_rent_duration(self, duration):
        options = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(OrderPageLocators.RENT_TIME_OPTIONS))
        for item in options:
            if item.text == duration:
                item.click()
                return
        raise Exception(f"Срок аренды '{duration}' не найден")



    @allure.step("Заполнение второй формы: 'Про аренду'")
    def fill_second_form(self, date, duration, color_loc, comment):
        date_input = self.find_element(OrderPageLocators.DATE_FIELD)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        self.click(OrderPageLocators.RENT_TIME_FIELD)
        self.select_rent_duration(duration)
        self.click(color_loc)
        self.find_element(OrderPageLocators.COMMENT_FIELD).send_keys(comment)
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверка успешного оформления заказа")
    def check_success(self):
        return self.find_element(OrderPageLocators.SUCCESS_HEADER)
