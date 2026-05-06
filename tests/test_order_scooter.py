import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData
import allure


class TestOrderScooter:

    @allure.title("Проверка полного цикла заказа самоката")
    @pytest.mark.parametrize("button_location, data", [("top", OrderData.DATA_SET_1),("bottom", OrderData.DATA_SET_2)])

    def test_full_order_flow_success(self, driver, button_location, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()     #открытие главной страницы
        main_page.accept_cookies()     #подтверждение куки для избежания конфликта интерфейса
        main_page.click_order_button(button_location)   #клик по кнопке

        # Данные из словаря data.py
        order_page.fill_first_form(data["name"], data["surname"], data["address"], data["station"], data["phone"])
        order_page.fill_second_form(data["date"], data["duration"], data["color"], data["comment"])

        order_page.confirm()                #подтверждение заказа
        assert order_page.check_success()   #проверка успешного заказа
