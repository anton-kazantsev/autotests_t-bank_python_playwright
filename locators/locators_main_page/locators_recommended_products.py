from locators.base_locator import BaseLocator


class LocatorRecommendedProducts:

    communication = BaseLocator(
        selector='Связь в 2',
        description="Переход по ссылке Связь в 2 раза дешевле"
    )

    deposits = BaseLocator(
        selector="Откройте вклад",
        description="Переход по ссылке Вклады"
    )

    products = BaseLocator(
        selector="Все продукты",
        description="Переход по ссылке Все продукты"
    )

    # Локаторы проверки открытых страниц
    heading_credit_communication = BaseLocator(
        selector='role=heading[name="Мобильная связь в 2 раза дешевле"]',
        description="Заголовок Мобильная связь в 2 раза дешевле"
    )

    heading_deposits = BaseLocator(
        selector='role=heading[name="Вклады со ставкой до 19% годовых"]',
        description="Заголовок Вклады со ставкой"
    )

    heading_all_products = BaseLocator(
        selector="role=heading[name='Рекомендуемые продукты']",
        description="Заголовок Рекомендуемые продукты"
    )