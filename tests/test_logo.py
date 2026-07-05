from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogos:

    def test_scooter_logo_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_cookie_accept()
        main_page.click_element_with_wait(main_page.TOP_ORDER_BUTTON)
        main_page.click_scooter_logo()

        assert driver.current_url == main_page.URL

    def test_yandex_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))

        assert "dzen.ru" in driver.current_url