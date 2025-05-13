from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from locators.locators_main_page.locators_mobile_app import LocatorApp


class AppPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page1 = page

    def open_android(self):
        """
        Открытие страницы android
        """
        self.open("")
        self.click_by_title(LocatorApp.button_android.selector)
        self.expect_locator(LocatorApp.header_android.selector)

    def open_ios(self):
        """
        Открытие страницы ios
        """
        self.open("")
        self.click_by_title(LocatorApp.button_ios.selector)
        self.expect_locator(LocatorApp.header_ios.selector)

    def open_app_gallery(self):
        self.open("")
        new_page = self.open_new_page(LocatorApp.button_app_gallery.selector)
        expect(new_page.locator(LocatorApp.title_app_gallery.selector)).to_be_visible()