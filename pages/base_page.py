import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента с ожиданием")
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу с ожиданием")
    def click_element_with_wait(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключение на новую вкладку")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ожидание изменения URL")
    def wait_for_url_contains(self, url_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_text))

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url