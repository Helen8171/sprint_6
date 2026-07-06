import allure
from pages.main_page import MainPage
from urls import Urls


class TestLogos:

    @allure.title("Проверка клика по логотипу Самоката")
    def test_scooter_logo_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_cookie_accept()
        main_page.click_order_button("top")
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.title("Проверка клика по логотипу Яндекса")
    def test_yandex_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.open()

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_for_url_contains(Urls.DZEN_URL)

        assert Urls.DZEN_URL in main_page.get_current_url()