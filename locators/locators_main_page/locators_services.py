from locators.base_locator import BaseLocator


class LocatorServices:

    currency_rate = BaseLocator(
        selector="Перевод между своими счетами, оплата услуг и снятие наличных в сервисах Т‑Банка",
        description="Открытие курсов валют"
    )

    cash_withdrawal = BaseLocator(
        selector="В банкоматах Т‑Банка без комиссии. И без карты, если у вас смартфон",
        description="Открытие Снятие наличных"
    )

    mortgage_repayment = BaseLocator(
        selector="Оформите полис до 31 мая и участвуйте в розыгрыше",
        description="Погашение ипотеки"
    )

    more_articles = BaseLocator(
        selector="Больше статей",
        description="Больше статей"
    )

    # Заголовки открытых страниц

    header_currency_rate = BaseLocator(
        selector=".irod3t:has-text('Курсы популярных валют для частных лиц')",
        description="Заголовок Курсы валют"
    )

    header_cash_withdrawal = BaseLocator(
        selector=".UnitedMapBack__title_woYeO:has-text('Банкоматы и партнеры')",
        description="Заголовок Банкоматы и партнеры"
    )

    header_mortgage_repayment = BaseLocator(
        selector="role=heading[name='Каждые два месяца разыгрываем до 3 000 000 ₽ на погашение ипотеки']",
        description="Заголовок Каждые два месяца разыгрываем до 3 000 000 ₽ на погашение ипотеки"
    )

    header_more_articles = BaseLocator(
        selector="role=heading[name='Т‑Блог']",
        description="Заголовок Т‑Блог"
    )