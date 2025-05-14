from pages.main_page.additionally_page import AdditionallyPage
from playwright.sync_api import Page


class TestAdditionally:

    def test_open_help(self, page: Page):
        helps = AdditionallyPage(page)
        helps.open_help()

    def test_open_reviews(self, page: Page):
        reviews = AdditionallyPage(page)
        reviews.open_reviews()