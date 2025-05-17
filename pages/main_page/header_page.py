from playwright.sync_api import Page
from locators.locators_main_page.locators_header import LocatorsHeader as Loc
from pages.base_page import BasePage


class HeaderPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_still_header(self):
        """
        Наведение на Еще в хэдере
        """
        self.open("")
        self.hover_choice_locator(locator=Loc.still_header.selector)

    def open_products_for_individuals(self):
        """
        Открытие Продукты для физлиц
        """
        self.click_choice_locator(locator=Loc.products_for_individuals.selector)
        self.expect_to_visible_choice_locator(locator=Loc.header_t_help_bank.selector)