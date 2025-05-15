from playwright.sync_api import Page
from locators.locators_main_page.locators_header import LocatorsHeader
from pages.base_page import BasePage


class HeaderPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_still_header(self):
        """
        Наведение на Еще в хэдере
        """
        self.open("")
        self.hover_on_element(LocatorsHeader.still_header.selector)
        self.click_locator(LocatorsHeader.products_for_individuals.selector)
        self.expect_locator(LocatorsHeader.header_t_help_bank.selector)