from pages.points_of_replenishment_page import ReplenishmentPage
from playwright.sync_api import Page


class TestReplenishment:

    def test_atm_search(self, page: Page):
        atm = ReplenishmentPage(page)
        atm.open_map()
        atm.click_take()
        atm.click_currency()
        atm.choice_dollars()
        atm.input_summ()
        atm.choosing_bank()