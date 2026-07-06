import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:

    @allure.title("Оформление заказа через разные кнопки")
    @pytest.mark.parametrize(
        "button, name, surname, address, phone, comment",
        [
            ("top", "Иван", "Иванов", "Москва, ул. Пушкина 1", "+79991112233", "Жду самокат"),
            ("bottom", "Анна", "Смирнова", "Москва, ул. Ленина 2", "+79995556677", "Позвоните за час")
        ]
    )
    def test_order_scooter_success(self, driver, button, name, surname, address, phone, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.click_cookie_accept()

        main_page.click_order_button(button)

        order_page.fill_personal_info(name, surname, address, phone)
        order_page.fill_rent_info(comment)

        assert order_page.is_success_modal_displayed()