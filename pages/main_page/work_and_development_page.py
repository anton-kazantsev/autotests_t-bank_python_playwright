from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from locators.locators_main_page.locators_work_and_development import LocatorsWork


class WorkPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    def open_work(self):
        """
        Открыть вакансии
        """
        self.open("")
        self.click_choice_locator(locator=LocatorsWork.work.selector)
        self.expect_to_visible_choice_locator(locator=LocatorsWork.header_work.selector)

    def open_education(self):
        """
        Открыть Т-Образование
        """
        self.open("")
        new_page = self.open_new_page_after_click_choice_locator(role=self.link, name=LocatorsWork.education.selector)
        expect(new_page.locator(LocatorsWork.header_education.selector)).to_be_visible()

    def open_use_credit(self):
        """
        Открыть Как пользоваться кредиткой
        """
        self.open("")
        new_page = self.open_new_page_after_click_choice_locator(role=self.link, name=LocatorsWork.use_credit.selector)
        expect(new_page.locator(LocatorsWork.header_use_credit.selector)).to_be_visible()