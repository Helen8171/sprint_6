import pytest
from pages.main_page import MainPage

class TestQuestions:

    @pytest.mark.parametrize(
        "question_number, expected_text",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")
        ]
    )
    def test_faq_answers(self, driver, question_number, expected_text):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_cookie_accept()
        main_page.click_question(question_number)
        actual_text = main_page.get_answer_text(question_number)
        assert actual_text == expected_text