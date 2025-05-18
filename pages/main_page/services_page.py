from playwright.sync_api import Page
from locators.locators_main_page.locators_services import LocatorServices
from pages.base_page import BasePage


class ServicesPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_currency_rate(self):
        """
        Открытие курсов валют
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=LocatorServices.currency_rate.selector)
        self.expect_to_visible_choice_locator(locator=LocatorServices.header_currency_rate.selector)

    def open_cash_withdrawal(self):
        """
        Открытие Снятие наличных
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=LocatorServices.cash_withdrawal.selector)
        self.expect_to_visible_choice_locator(locator=LocatorServices.header_cash_withdrawal.selector)

    def open_mortgage_repayment(self):
        """
        Открытие Погашение ипотеки
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=LocatorServices.mortgage_repayment.selector)
        self.expect_to_visible_choice_locator(locator=LocatorServices.header_mortgage_repayment.selector)

    def open_more_articles(self):
        """
        Открытие Больше статей
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=LocatorServices.more_articles.selector)
        self.expect_to_visible_choice_locator(locator=LocatorServices.header_more_articles.selector)
