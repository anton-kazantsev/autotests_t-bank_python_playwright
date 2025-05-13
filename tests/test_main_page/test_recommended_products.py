import pytest
from pages.main_page.recommended_products_page import RecommendedProductPage as RecProdPage
from playwright.sync_api import Page


class TestRecommendedProducts:

    def test_open_communication(self, page: Page):
        communication = RecProdPage(page)
        communication.open_communication()

    def test_open_deposits_recommended(self, page: Page):
        deposits = RecProdPage(page)
        deposits.open_deposits_recommended()

    def test_open_all_products(self, page: Page):
        insurance = RecProdPage(page)
        insurance.open_all_products()