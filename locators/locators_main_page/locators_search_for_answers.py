from locators.base_locator import BaseLocator


class LocatorsSearch:

    fill_search = BaseLocator(
        selector="Ипотека на вторичное жилье Кредиты • Ипотека",
        description="Выбор первой строки в выпадающем списке"
    )

    button_how_input_in_account = BaseLocator(
        selector="role=button[name='Как войти в личный кабинет']",
        description="Кнопка Как войти в личный кабинет"
    )

    click_input_in_account = BaseLocator(
        selector="Как войти в личный кабинет Интерфейсы • Личный кабинет",
        description="Выбор первой строки в выпадающем списке"
    )

    # Заголовки проверки открытия страниц

    headed_search = BaseLocator(
        selector="role=heading[name='Ипотека на вторичное жилье']",
        description="Ипотека на вторичное жилье"
    )

    headed_input_in_account = BaseLocator(
        selector="role=heading[name='Как войти в личный кабинет']",
        description="Заголовок Как войти в личный кабинет"
    )