from locators.base_locator import BaseLocator


class LocatorsHorizontalMenu:
    panel_slides = BaseLocator(
        selector="[data-test=\"panel slides\"]",
        description="Горизонтальная панель"
    )

    debit_cards = BaseLocator(
        selector='[data-test="panel slides"] >> role=link[name="Дебетовые карты"]',
        description="Ссылка 'Дебетовые карты' в горизонтальном меню"
    )

    heading_debit_cards = BaseLocator(
        selector='role=heading[name="Дебетовые карты"]',
        description="Заголовок Дебетовые карты"
    )