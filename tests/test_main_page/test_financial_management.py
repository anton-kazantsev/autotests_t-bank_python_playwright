import pytest
from pages.main_page.financial_managment_page import FinancialManagementPage as FinManPage
from playwright.sync_api import Page


class TestFinancialManagement:

    def test_fill_edit_deposit_in_rub(self, page: Page):
        deposit = FinManPage(page)
        deposit.open_main_page()
        deposit.click_checkbox_deposit()
        deposit.fill_edit_deposit()
        deposit.fill_edit_sum_deposit()
