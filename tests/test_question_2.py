import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import TextData


@allure.title("Проверка ответа на 2-й вопрос в Вопросы о важном")
@pytest.mark.parametrize("question, answer, expected", [(MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, TextData.ANSWER_2)])
def test_faq_answer(driver, question, answer, expected):
    main_page = MainPage(driver)
    main_page.open_main_page()  #открытие главной страницы
    main_page.accept_cookies()  #подтверждение куки для избежания конфликта интерфейса
    
    result = main_page.get_answer(question, answer)
    assert result == expected
