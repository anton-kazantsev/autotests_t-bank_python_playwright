from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from data.base_data import base_url
from locators.locators_main_page.locators_horizontal_menu import LocatorsHorizontalMenu


class HorizontalMenuPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_debit_cards(self):
        self.page.goto(base_url)
        self.page.locator(LocatorsHorizontalMenu.panel_slides.selector).click()
        expect(self.page.locator(LocatorsHorizontalMenu.debit_cards.selector)).to_be_visible()