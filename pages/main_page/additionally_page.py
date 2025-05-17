from playwright.sync_api import Page
from locators.locators_main_page.locators_additionally import LocatorsAdditionally as Loc
from pages.base_page import BasePage


class AdditionallyPage(BasePage):

    link = 'link'

    def __init__(self, page: Page):
        super().__init__(page)

    def open_help(self):
        """
        Открытие Помощь
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=Loc.helps.selector)
        self.expect_to_visible_choice_locator(locator=Loc.headers_helps.selector)

    def open_reviews(self):
        """
        Открытие Отзывы
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=Loc.reviews.selector)
        self.expect_to_visible_choice_locator(locator=Loc.headers_reviews.selector)