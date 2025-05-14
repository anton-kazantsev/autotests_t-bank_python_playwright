from playwright.sync_api import Page, Response, expect
from data import base_data
from typing import Optional


expect.set_options(timeout=30000)
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

    def fill_placeholder(self, loc, name, fill):
        """
        Заполнение плейсхолдера
        """
        return self.page.locator(loc).content_frame.get_by_role("textbox", name=name).fill(fill)

    def checkbox_uncheck(self, loc, name):
        """
        Нажатие на чекбокс
        """
        return self.page.locator(loc).content_frame.get_by_role("checkbox", name=name).uncheck()

    def click_by_role_link(self, sort, name):
        """
        Клик на элемент по роли
        """
        return self.page.get_by_role(sort, name=name).click()

    def click_by_title(self, title):
        """
        Клик по элементу с нужным тайтлом
        """
        return self.page.get_by_title(title).click()

    def open_new_page(self, title):
        """
        Клик на тайтл и открытие новой вклвдки
        """
        with self.page.expect_popup() as popup_info:
            self.page.get_by_title(title).click()
        new_page = popup_info.value
        return new_page

    def open_new_page_after_click_by_role(self, sort, name):
        """
        Клик на роль и открытие новой страницы
        """
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role(sort, name=name).click()
        new_page = popup_info.value
        return new_page

    def open_by_test_id(self, loc):
        """
        Клик по элементу с testID
        """
        return self.page.get_by_test_id(loc).click()