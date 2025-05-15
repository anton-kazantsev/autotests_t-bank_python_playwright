from locators.base_locator import BaseLocator


class LocatorsHeader:

    still_header = BaseLocator(
        selector="[data-test=menu] >> [data-test=menu-item-3]",
        description="Ссылка Еще в хэдере"
    )

    products_for_individuals = BaseLocator(
        selector="[data-test=menu-item-3-popover] >> [data-test=text-item-2-0-text]",
        description="Продукты для физлиц"
    )

    # Заголовки для проверки открытых страниц

    header_t_help_bank = BaseLocator(
        selector="role=heading[name='Т‑Помощь. Банк']",
        description="Т‑Помощь. Банк"
    )