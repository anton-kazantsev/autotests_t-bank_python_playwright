from locators.locators_main_page.locators_recommended_products import LocatorRecommendedProducts as Loc
from playwright.sync_api import Page
from pages.base_page import BasePage


class RecommendedProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_communication(self):
        """
        Открытие продукта Связь в 2 раза дешевле
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=Loc.communication.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_credit_communication.selector)

    def open_deposits_recommended(self):
        """
        Открытие Вклады в рекомендациях
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=Loc.deposits.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_deposits.selector)

    def open_all_products(self):
        """
        Открытие страницы страхования ипотеки
        """
        self.open("")
        self.click_choice_locator(role=self.link, name=Loc.products.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_all_products.selector)