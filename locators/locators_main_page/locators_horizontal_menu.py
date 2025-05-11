from locators.base_locator import BaseLocator


class LocatorsHorizontalMenu:
    panel_slides = BaseLocator(
        selector='[data-test="panel slides"]',
        description="Горизонтальная панель"
    )

    # Ссылки в горизонтальном меню
    debit_cards = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Дебетовые карты"]',
        description="Ссылка 'Дебетовые карты' в горизонтальном меню"
    )

    credit_cards = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Кредитные карты"]',
        description="Ссылка 'Кредитные карты' в горизонтальном меню"
    )

    credit = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Кредиты"]',
        description="Ссылка 'Кредиты' в горизонтальном меню"
    )

    premium = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Премиум"]',
        description="Ссылка 'Премиум' в горизонтальном меню"
    )

    deposits = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Вклады"]',
        description="Ссылка 'Вклады' в горизонтальном меню"
    )

    investment = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Инвестиции"]',
        description="Ссылка 'Инвестиции' в горизонтальном меню"
    )

    sim_card = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Сим-карта"]',
        description="Ссылка 'Сим-карта' в горизонтальном меню"
    )

    insurance = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Страхование"]',
        description="Ссылка 'Страхование' в горизонтальном меню"
    )

    journeys = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Путешествия"]',
        description="Ссылка 'Путешествия' в горизонтальном меню"
    )

    for_business = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Всё для Бизнеса"]',
        description="Ссылка 'Всё для Бизнеса' в горизонтальном меню"
    )

    # Локаторы проверки открытых страниц

    heading_debit_cards = BaseLocator(
        selector='role=heading[name="Дебетовые карты"]',
        description="Заголовок Дебетовые карты"
    )

    heading_credit_cards = BaseLocator(
        selector='role=heading[name="Кредитные карты"]',
        description="Заголовок Кредитные карты"
    )

    heading_credits = BaseLocator(
        selector='role=heading[name="Кредиты на любые цели"]',
        description="Заголовок Кредиты на любые цели"
    )

    heading_premium = BaseLocator(
        selector='role=heading[name="Premium"]',
        description="Заголовок Premium"
    )

    heading_deposits = BaseLocator(
        selector='role=heading[name="Вклады со ставкой до 19% годовых"]',
        description="Заголовок Вклады со ставкой до 19% годовых"
    )

    heading_investment = BaseLocator(
        selector='role=heading[name="Т-Инвестиции"]',
        description="Заголовок Т-инвестиции"
    )

    heading_sim_card = BaseLocator(
        selector='role=heading[name="Мобильная связь в 2 раза дешевле"]',
        description="Заголовок Мобильная связь в 2 раза дешевле"
    )

    heading_insurance = BaseLocator(
        selector='role=heading[name="Страховые продукты Т-Страхования"]',
        description="Заголовок Страховые продукты Т-Страхования"
    )
    heading_journeys = BaseLocator(
        selector='role=heading[name="Ваше путешествие начинается здесь"]',
        description='Заголовок Ваше путешествие начинается здесь'
    )

    heading_for_business = BaseLocator(
        selector='role=heading[name="Онлайн-банк для малого бизнеса"]',
        description="Заголовок Онлайн-банк для малого бизнеса"
    )