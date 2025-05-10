from playwright.sync_api import Page, Response
from data import base_data
from typing import Optional


class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url: str = base_data.base_url

    def open(self, uri: str) -> Optional[Response]:
        return self.page.goto(f"{self.base_url}{uri}")