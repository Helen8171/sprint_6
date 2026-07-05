from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    TOP_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']/parent::a")
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']/parent::a")

    def open(self):
        self.driver.get(self.URL)

    def click_cookie_accept(self):
        try:
            self.click_element_with_wait(self.COOKIE_BUTTON, timeout=3)
        except:
            pass

    def format_question_locator(self, question_number):
        return By.ID, f"accordion__heading-{question_number}"

    def format_answer_locator(self, answer_number):
        return By.ID, f"accordion__panel-{answer_number}"

    def click_question(self, question_number):
        locator = self.format_question_locator(question_number)
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element_with_wait(locator)

    def get_answer_text(self, answer_number):
        locator = self.format_answer_locator(answer_number)
        return self.find_element_with_wait(locator).text

    def click_yandex_logo(self):
        self.click_element_with_wait(self.YANDEX_LOGO)

    def click_scooter_logo(self):
        self.click_element_with_wait(self.SCOOTER_LOGO)