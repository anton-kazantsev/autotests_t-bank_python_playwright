from locators.base_locator import BaseLocator


class LocatorsAdditionally:

    helps = BaseLocator(
        selector="Помощь Отвечаем на вопросы по всем продуктам",
        description="Помощь Отвечаем на вопросы по всем продуктам"
    )

    reviews = BaseLocator(
        selector="Т‑Банк Отзывы Выбирайте продукты Т‑Банк, магазины, рестораны,"
                 " сервисы и бренды на основе реальных отзывов",
        description="Т-Банк Отзывы"
    )

    # Заголовки проверки открытых страниц

    headers_helps = BaseLocator(
        selector="role=heading[name='Т‑Помощь']",
        description="Заголовок Т‑Помощь"
    )

    headers_reviews = BaseLocator(
        selector="role=heading[name='Т-Банк Отзывы']",
        description="Заголовок"
    )