from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage(BasePage):

    @allure.step("Заполнение первой формы: 'Для кого самокат'")
    def fill_first_form(self, name, surname, address, station, phone):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)
        self.send_keys(OrderPageLocators.SURNAME_FIELD, surname)
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)
        self.select_metro_station(station)
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбор станции метро: {station}")
    def select_metro_station(self, station):
        self.click_order(OrderPageLocators.METRO_FIELD)
        self.send_keys(OrderPageLocators.METRO_FIELD, station)
        metro_input = self.find_element(OrderPageLocators.METRO_FIELD)
        metro_input.send_keys(Keys.DOWN)
        metro_input.send_keys(Keys.ENTER)
    
    @allure.step("Выбор срока аренды: {duration}")
    def select_rent_duration(self, duration):
        self.click_order(OrderPageLocators.RENT_TIME_FIELD)
        options = self.find_elements(OrderPageLocators.RENT_TIME_OPTIONS)
        for item in options:
            if item.text == duration:
                item.click()
                return
    
    @allure.step("Выбор цвета самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)
    
    @allure.step("Заполнение второй формы: 'Про аренду'")
    def fill_second_form(self, date, duration, color, comment):
        self.send_keys(OrderPageLocators.DATE_FIELD, date)
        self.find_element(OrderPageLocators.DATE_FIELD).send_keys(Keys.ENTER)
        self.select_rent_duration(duration)
        self.select_color(color)
        self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверка успешного оформления заказа")
    def check_success(self):
        return self.find_element(OrderPageLocators.SUCCESS_HEADER)
