from pages.base_page import BasePage
from playwright.sync_api import Page
from locators.locators_main_page.locators_financial_management import FinancialManagementLocator as FinManLoc
from data.constants import Constants


class FinancialManagementPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_main_page(self):
        """
        Открытие главной страницы
        """
        self.open("")

    def fill_edit_deposit(self):
        """
        Заполнение срока вклада
        """
        self.fill_placeholder(FinManLoc.container_fin_management.selector, Constants.deposit_period, "5")

    def fill_edit_sum_deposit(self):
        """
        Заполнение суммы вклада
        """
        self.fill_placeholder(FinManLoc.container_fin_management.selector, Constants.sum_deposit, "10 000 000")

    def click_checkbox_deposit(self):
        """
        Нажатие на чекбокс Непополняемый депозит
        """
        self.checkbox_uncheck(FinManLoc.container_fin_management.selector, Constants.checkbox_non_refillable_deposit)