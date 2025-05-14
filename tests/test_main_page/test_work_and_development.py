from playwright.sync_api import Page
from pages.main_page.work_and_development_page import WorkPage


class TestWork:

    def test_open_work(self, page: Page):
        work = WorkPage(page)
        work.open_work()

    def test_open_education(self, page: Page):
        education = WorkPage(page)
        education.open_education()

    def test_open_use_credit(self, page: Page):
        use_credit = WorkPage(page)
        use_credit.open_use_credit()