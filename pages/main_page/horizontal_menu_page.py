from pages.base_page import BasePage
from playwright.sync_api import Page
from locators.locators_main_page.locators_horizontal_menu import LocatorsHorizontalMenu


class HorizontalMenuPage(BasePage):

    slides = LocatorsHorizontalMenu

    def __init__(self, page: Page):
        super().__init__(page)

    def open_debit_cards(self):
        """
        Переход на страницу Дебетовые карты через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.debit_cards.selector)
        self.expect_locator(self.slides.heading_debit_cards.selector)


    def open_credit_cards(self):
        """
        Переход на страницу Кредитные карты через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.credit_cards.selector)
        self.expect_locator(self.slides.heading_credit_cards.selector)

    def open_credits(self):
        """
         Переход на страницу Кредиты через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.credit.selector)
        self.expect_locator(self.slides.heading_credits.selector)

    def open_premium(self):
        """
        Переход на страницу Премиум через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.premium.selector)
        self.expect_locator(self.slides.heading_premium.selector)

    def open_deposits(self):
        """
        Переход на страницу Вклады через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.deposits.selector)
        self.expect_locator(self.slides.heading_deposits.selector)

    def open_investment(self):
        """
        Переход на страницу Инвестиции через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.investment.selector)
        self.expect_locator(self.slides.heading_investment.selector)

    def open_sim_card(self):
        """
        Переход на страницу Сим-карта через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.sim_card.selector)
        self.expect_locator(self.slides.heading_sim_card.selector)

    def open_insurance(self):
        """
        Переход на страницу Страхование через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.insurance.selector)
        self.expect_locator(self.slides.heading_insurance.selector)

    def open_journeys(self):
        """
        Переход на страницу Путешествия через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.journeys.selector)
        self.expect_locator(self.slides.heading_journeys.selector)

    def open_everything_for_business(self):
        """
        Переход на страницу Всё для бизнеса через горизонтальное меню на главной странице
        """
        self.open("")
        self.click_locator(self.slides.for_business.selector)
        self.expect_locator(self.slides.heading_for_business.selector)