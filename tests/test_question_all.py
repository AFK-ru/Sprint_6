import pytest
import allure
from pages.main_page import MainPage
from data import TextData

class TestFAQ:

    @allure.title("Проверка ответов в FAQ")
    @pytest.mark.parametrize("index, expected", [
        (0, TextData.ANSWER_1),
        (1, TextData.ANSWER_2),
        (2, TextData.ANSWER_3),
        (3, TextData.ANSWER_4),
        (4, TextData.ANSWER_5),
        (5, TextData.ANSWER_6),
        (6, TextData.ANSWER_7),
        (7, TextData.ANSWER_8)
    ])
    
    def test_faq_answers(self, driver, index, expected):
        main_page = MainPage(driver)
        main_page.open_main_page()    #открытие главной страницы
        main_page.accept_cookies()    #подтверждение куки для избежания конфликта интерфейса
        
        assert main_page.get_answer_text(index) == expected   #проверка соответствия вопросу текста ответа
