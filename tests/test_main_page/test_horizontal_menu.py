from playwright.sync_api import Page
from pages.main_page.horizontal_menu_page import HorizontalMenuPage
import pytest


@pytest.mark.smoke
class TestHorizontalMenu:

    slides = HorizontalMenuPage

    def test_debit_cards(self, page: Page):
        debit = self.slides(page)
        debit.open_debit_cards()

    def test_credit_cards(self, page: Page):
        credit = self.slides(page)
        credit.open_credit_cards()

    def test_credits(self, page: Page):
        credit = self.slides(page)
        credit.open_credits()

    def test_premium(self, page: Page):
        premium = self.slides(page)
        premium.open_premium()

    def test_open_deposits(self, page: Page):
        deposits = self.slides(page)
        deposits.open_deposits()

    def test_open_investment(self, page: Page):
        investment = self.slides(page)
        investment.open_investment()

    def test_open_sim_card(self, page: Page):
        sim_card = self.slides(page)
        sim_card.open_sim_card()

    def test_open_insurance(self, page: Page):
        insurance = self.slides(page)
        insurance.open_insurance()

    def test_open_journeys(self, page: Page):
        journeys = self.slides(page)
        journeys.open_journeys()

    def test_open_for_business(self, page: Page):
        for_business = self.slides(page)
        for_business.open_everything_for_business()