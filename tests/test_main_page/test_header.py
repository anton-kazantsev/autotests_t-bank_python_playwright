from pages.main_page.header_page import HeaderPage
from playwright.sync_api import Page


class TestHeader:

    def test_open_products_for_individuals(self, page: Page):
        products = HeaderPage(page)
        products.open_still_header()