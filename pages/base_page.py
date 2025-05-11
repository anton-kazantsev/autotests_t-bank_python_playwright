from playwright.sync_api import Page, Response, expect
from data import base_data
from typing import Optional


class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url: str = base_data.base_url

    def open(self, uri: str) -> Optional[Response]:
        """
        Переход на конкретную страницу сайта
        """
        return self.page.goto(f"{self.base_url}{uri}")

    def click_locator(self, loc):
        """
        Клик на локатор
        """
        return self.page.locator(loc).click()

    def expect_locator(self, loc):
        """
        Ожидание локатора
        """
        return expect(self.page.locator(loc)).to_be_visible()