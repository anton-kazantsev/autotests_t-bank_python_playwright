from pages.main_page.mobile_app_page import AppPage
from playwright.sync_api import Page


class TestApp:

    def test_open_android(self, page: Page):
        android = AppPage(page)
        android.open_android()

    def test_open_ios(self, page: Page):
        ios = AppPage(page)
        ios.open_ios()

    def test_open_app_gallery(self, page: Page):
        app_gallery = AppPage(page)
        app_gallery.open_app_gallery()