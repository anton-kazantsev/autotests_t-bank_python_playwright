from playwright.sync_api import Page
from pages.main_page.horizontal_menu_page import HorizontalMenuPage


class TestHorizontalMenu:
    def test_debit_cards(self, page: Page):
        debit = HorizontalMenuPage(page)
        debit.open_debit_cards()
