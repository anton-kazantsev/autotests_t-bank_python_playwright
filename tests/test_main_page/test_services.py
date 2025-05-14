from pages.main_page.services_page import ServicesPage
from playwright.sync_api import Page


class TestServices:

    def test_open_currency_rate(self, page: Page):
        currency = ServicesPage(page)
        currency.open_currency_rate()

    def test_open_cash_withdrawal(self, page: Page):
        cash_withdrawal = ServicesPage(page)
        cash_withdrawal.open_cash_withdrawal()

    def test_open_mortgage_repayment(self, page: Page):
        mortgage_repayment = ServicesPage(page)
        mortgage_repayment.open_mortgage_repayment()

    def test_open_more_articles(self, page: Page):
        articles = ServicesPage(page)
        articles.open_more_articles()