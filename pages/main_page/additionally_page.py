from playwright.sync_api import Page
from locators.locators_main_page.locators_additionally import LocatorsAdditionally
from pages.base_page import BasePage


class AdditionallyPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_help(self):
        """
        Открытие Помощь
        """
        self.open("")
        self.click_by_role_link("link", LocatorsAdditionally.helps.selector)
        self.expect_locator(LocatorsAdditionally.headers_helps.selector)

    def open_reviews(self):
        """
        Открытие Отзывы
        """
        self.open("")
        self.click_by_role_link("link", LocatorsAdditionally.reviews.selector)
        self.expect_locator(LocatorsAdditionally.headers_reviews.selector)