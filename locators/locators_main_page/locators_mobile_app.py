from locators.base_locator import BaseLocator


class LocatorApp:

    button_android = BaseLocator(
        selector="Скачать приложение Т-Банка для Android",
        description="Кнопка android"
    )

    button_ios = BaseLocator(
        selector="Скачать приложение Т-Банка для IOS",
        description="Кнопка ios"
    )

    button_app_gallery = BaseLocator(
        selector="Скачать приложение Т-Банка из AppGallery",
        description="Кнопка AppGallery"
    )

    # Локаторы проверки открытых страниц

    header_android = BaseLocator(
        selector="role=heading[name='Скачайте приложение Т‑Банка на Android']",
        description="Заголовок Скачайте приложение Т‑Банка на Android"
    )

    header_ios = BaseLocator(
        selector="role=heading[name='Скачайте приложение Т‑Банка на iOS']",
        description="Заголовок Скачайте приложение Т-Банка на iOS"
    )

    title_app_gallery = BaseLocator(
        selector="div.detailheadcard:has-text('Т-Банк')",
        description="Тайтл Т-Банк"
    )