from playwright.sync_api import sync_playwright
import pytest
from conftest import context


@pytest.fixture(scope="function")
with context.()