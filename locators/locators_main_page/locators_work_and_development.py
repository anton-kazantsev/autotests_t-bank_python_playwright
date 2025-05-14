from locators.base_locator import BaseLocator


class LocatorsWork:

    work = BaseLocator(
        selector=".ebRTuR07k:has-text('Смотреть вакансии')",
        description="Вакансии"
    )

    education = BaseLocator(
        selector="Учебные курсы и оплачиваемые программы развития",
        description="Т-Образование"
    )

    use_credit = BaseLocator(
        selector="Т—Ж",
        description="Как пользоваться кредиткой"
    )

    # Заголовки открытых страниц

    header_work = BaseLocator(
        selector="role=heading[name='Работа в Т-Банке']",
        description="Заголовок Работа в Т-Банке"
    )

    header_education = BaseLocator(
        selector="role=heading[name='Т‑Образование']",
        description="Заголовок Образование"
    )

    header_use_credit = BaseLocator(
        selector="role=heading[name='Как на самом деле пользоваться кредиткой']",
        description="Заголовок Как на самом деле пользоваться кредиткой"
    )