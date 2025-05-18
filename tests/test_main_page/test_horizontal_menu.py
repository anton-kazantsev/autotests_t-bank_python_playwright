from playwright.sync_api import Page
from pages.main_page.horizontal_menu_page import HorizontalMenuPage


class TestHorizontalMenu:

    def test_debit_cards(self, page: Page):
        debit = HorizontalMenuPage(page)
        debit.open_debit_cards()

    def test_credit_cards(self, page: Page):
        credit = HorizontalMenuPage(page)
        credit.open_credit_cards()

    def test_credits(self, page: Page):
        credit = HorizontalMenuPage(page)
        credit.open_credits()

    def test_premium(self, page: Page):
        premium = HorizontalMenuPage(page)
        premium.open_premium()

    def test_open_deposits(self, page: Page):
        deposits = HorizontalMenuPage(page)
        deposits.open_deposits()

    def test_open_investment(self, page: Page):
        investment = HorizontalMenuPage(page)
        investment.open_investment()

    def test_open_sim_card(self, page: Page):
        sim_card = HorizontalMenuPage(page)
        sim_card.open_sim_card()

    def test_open_insurance(self, page: Page):
        insurance = HorizontalMenuPage(page)
        insurance.open_insurance()

    def test_open_journeys(self, page: Page):
        journeys = HorizontalMenuPage(page)
        journeys.open_journeys()

    def test_open_for_business(self, page: Page):
        for_business = HorizontalMenuPage(page)
        for_business.open_everything_for_business()