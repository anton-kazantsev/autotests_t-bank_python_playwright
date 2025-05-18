from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.locators_points_of_replenishment import LocatorsReplenishment as Loc
from data.base_data import uri_points_of_replenishment


class ReplenishmentPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_map(self):
        """
        Открытие карты банкоматов и партнеров
        """
        self.open(uri_points_of_replenishment)

    def click_take(self):
        """
        Нажать Снять
        """
        self.click_choice_locator(locator=Loc.click_take.selector)

    def click_currency(self):
        """
        Нажать на выбор валюты
        """
        self.click_choice_locator(role=self.button, name=Loc.input_choice.selector)

    def choice_dollars(self):
        """
        Выбор валюты Доллары
        """
        self.click_choice_locator(role=self.option, name=Loc.choice_dollars.selector)

    def input_summ(self):
        """
        Ввод суммы для снятия средств
        """
        self.fill_choice_locator(locator=Loc.placeholder_summ.selector, fill=Loc.input_summ.selector)

    def choosing_bank(self):
        """
        Выбор Т-Банк в списке банков
        """
        self.click_choice_locator(locator=Loc.choosing_bank.selector)