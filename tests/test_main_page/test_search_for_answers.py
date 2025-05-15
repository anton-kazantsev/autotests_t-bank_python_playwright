from pages.main_page.search_for_answers_page import SearchPage
from playwright.sync_api import Page


class TestSearch:

    def test_input_search(self, page: Page):
        search = SearchPage(page)
        search.input_search()

    def test_open_how_input_in_account(self, page: Page):
        account = SearchPage(page)
        account.open_how_input_in_account()