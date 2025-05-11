import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext


@pytest.fixture(scope="session")
def browser():
    """Фикстура инициализации браузера"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def context(browser: Browser):
    """Фикстура создания контекста с настройками для Т-Банк"""
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext):
    """Фикстура открытия главной страницы Т-Банк"""
    page = context.new_page()
    yield page
    page.close()