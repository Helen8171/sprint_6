import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']/parent::a")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']/parent::a")

    @allure.step("Открытие главной страницы Самоката")
    def open(self):
        self.driver.get(Urls.MAIN_PAGE)

    @allure.step("Принятие куки")
    def click_cookie_accept(self):
        try:
            self.click_element_with_wait(self.COOKIE_BUTTON, timeout=3)
        except:
            pass

    @allure.step("Форматирование локатора вопроса")
    def format_question_locator(self, question_number):
        return By.ID, f"accordion__heading-{question_number}"

    @allure.step("Форматирование локатора ответа")
    def format_answer_locator(self, answer_number):
        return By.ID, f"accordion__panel-{answer_number}"

    @allure.step("Клик по вопросу номер {question_number}")
    def click_question(self, question_number):
        locator = self.format_question_locator(question_number)
        self.scroll_to_element(locator)
        self.click_element_with_wait(locator)

    @allure.step("Получение текста ответа номер {answer_number}")
    def get_answer_text(self, answer_number):
        locator = self.format_answer_locator(answer_number)
        return self.find_element_with_wait(locator).text

    @allure.step("Клик по кнопке Заказать ({button_position})")
    def click_order_button(self, button_position):
        if button_position == "top":
            self.click_element_with_wait(self.TOP_ORDER_BUTTON)
        elif button_position == "bottom":
            self.scroll_to_element(self.BOTTOM_ORDER_BUTTON)
            self.click_element_with_wait(self.BOTTOM_ORDER_BUTTON)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element_with_wait(self.YANDEX_LOGO)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element_with_wait(self.SCOOTER_LOGO)