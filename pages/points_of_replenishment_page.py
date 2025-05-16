from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.locators_points_of_replenishment import LocatorsReplenishment
from data.base_data import uri_points_of_replenishment


class ReplenishmentPage(BasePage):

    button = "button"
    option = "option"

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
        self.click(LocatorsReplenishment.click_take.selector)

    def click_currency(self):
        """
        Нажать на выбор валюты
        """
        self.click(LocatorsReplenishment.input_choice.selector, self.button)

    def choice_dollars(self):
        """
        Выбор валюты Доллары
        """
        self.click(LocatorsReplenishment.choice_dollars.selector, self.option)

    def input_summ(self):
        """
        Ввод суммы для снятия средств
        """
        self.fill_locator(LocatorsReplenishment.placeholder_summ.selector,
                          LocatorsReplenishment.input_summ.selector)

    def choosing_bank(self):
        """
        Выбор Т-Банк в списке банков
        """
        self.click_locator(LocatorsReplenishment.choosing_bank.selector)