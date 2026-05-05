import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import OrderData
import allure


class TestOrderScooter:

    @allure.title("Проверка флоу заказа самоката с двумя разными наборами данных")
    @pytest.mark.parametrize("order_button, name, surname, address, station, phone, date, duration, color, comment", [
            (MainPageLocators.ORDER_BUTTON_TOP, *OrderData.DATA_SET_1.values()),
            (MainPageLocators.ORDER_BUTTON_BOTTOM, *OrderData.DATA_SET_2.values())
        ])
    
    def test_full_order_flow_success(self, driver, order_button, name, surname, address, station, phone, date, duration, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()  #открытие главной страницы
        main_page.accept_cookies()  #подтверждение куки для избежания конфликта интерфейса

        main_page.scroll_to(order_button)  #скролл до выбранной кнопки для ее видимости 
        main_page.click(order_button)      #клик по кнопке

        order_page.fill_first_form(name, surname, address, station, phone)  #заполнение первой формы заказа

        order_page.fill_second_form(date, duration, color, comment)  #заполнение второй формы заказа

        order_page.confirm()  #подтверждение заказа

        assert order_page.check_success() #проверка успешного заказа
