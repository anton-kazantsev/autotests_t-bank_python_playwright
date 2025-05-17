from pages.base_page import BasePage
from playwright.sync_api import Page
from locators.locators_main_page.locators_horizontal_menu import LocatorsHorizontalMenu as Loc


class HorizontalMenuPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_debit_cards(self):
        """
        Переход на страницу Дебетовые карты через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.debit_cards.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_debit_cards.selector)


    def open_credit_cards(self):
        """
        Переход на страницу Кредитные карты через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.credit_cards.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_credit_cards.selector)

    def open_credits(self):
        """
         Переход на страницу Кредиты через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.credit.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_credits.selector)

    def open_premium(self):
        """
        Переход на страницу Премиум через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.premium.selector)
        self.expect_to_visible_choice_locator(text=Loc.heading_premium.selector)

    def open_deposits(self):
        """
        Переход на страницу Вклады через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.deposits.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_deposits.selector)

    def open_investment(self):
        """
        Переход на страницу Инвестиции через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.investment.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_investment.selector)

    def open_sim_card(self):
        """
        Переход на страницу Сим-карта через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.sim_card.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_sim_card.selector)

    def open_insurance(self):
        """
        Переход на страницу Страхование через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.insurance.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_insurance.selector)

    def open_journeys(self):
        """
        Переход на страницу Путешествия через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.journeys.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_journeys.selector)

    def open_everything_for_business(self):
        """
        Переход на страницу Всё для бизнеса через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_choice_locator(locator=Loc.for_business.selector)
        self.expect_to_visible_choice_locator(locator=Loc.heading_for_business.selector)