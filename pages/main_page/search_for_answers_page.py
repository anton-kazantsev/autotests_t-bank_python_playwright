from playwright.sync_api import Page
from locators.locators_main_page.locators_search_for_answers import LocatorsSearch
from pages.base_page import BasePage
from data.constants import Constants


class SearchPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def input_search(self):
        """
        Ввод вопроса в плейсхолдер
        """
        self.open("")
        self.fill_choice_locator(role=self.combobox, fill=Constants.text_search)
        self.click_choice_locator(role=self.option, name=LocatorsSearch.fill_search.selector)
        self.expect_to_visible_choice_locator(locator=LocatorsSearch.headed_search.selector)

    def open_how_input_in_account(self):
        """
        Нажатие на кнопку вопроса Как войти в личный кабинет
        """
        self.open("")
        self.click_choice_locator(locator=LocatorsSearch.button_how_input_in_account.selector)
        self.click_choice_locator(role=self.option, name=LocatorsSearch.click_input_in_account.selector)
        self.expect_to_visible_choice_locator(locator=LocatorsSearch.headed_input_in_account.selector)