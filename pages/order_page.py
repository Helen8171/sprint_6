from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, ".//div[@class='select-search__select']//li[@data-index='0']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_OPTION = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month'))]")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-root")
    RENTAL_OPTION = (By.XPATH, "//div[text()='сутки']")
    COLOR_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    def fill_personal_info(self, name, surname, address, phone):
        self.find_element_with_wait(self.FIRST_NAME_INPUT).send_keys(name)
        self.find_element_with_wait(self.LAST_NAME_INPUT).send_keys(surname)
        self.find_element_with_wait(self.ADDRESS_INPUT).send_keys(address)
        self.click_element_with_wait(self.METRO_INPUT)
        self.click_element_with_wait(self.METRO_OPTION)
        self.find_element_with_wait(self.PHONE_INPUT).send_keys(phone)
        self.click_element_with_wait(self.NEXT_BUTTON)

    def fill_rent_info(self, comment):
        self.click_element_with_wait(self.DATE_INPUT)
        self.click_element_with_wait(self.DATE_OPTION)

        self.find_element_with_wait(self.DATE_INPUT).send_keys(Keys.ENTER)

        self.click_element_with_wait(self.RENTAL_PERIOD)
        self.click_element_with_wait(self.RENTAL_OPTION)
        self.click_element_with_wait(self.COLOR_CHECKBOX)
        self.find_element_with_wait(self.COMMENT_INPUT).send_keys(comment)
        self.click_element_with_wait(self.ORDER_BUTTON)
        self.click_element_with_wait(self.CONFIRM_BUTTON)

    def is_success_modal_displayed(self):
        return self.find_element_with_wait(self.SUCCESS_MODAL).is_displayed()