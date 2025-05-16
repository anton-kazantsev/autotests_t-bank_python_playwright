from locators.base_locator import BaseLocator


class LocatorsReplenishment:

    placeholder = BaseLocator(
        selector="[id='dsId_R_B61csEaa']",
        description="Плейсхолдер ввода адреса"
    )

    click_take = BaseLocator(
        selector="role=button[name='Снять']",
        description="Кнопка Снять"
    )

    input_choice = BaseLocator(
        selector="Открыть",
        description="Выпадающий список выбора валют"
    )

    choice_dollars = BaseLocator(
        selector="Доллары",
        description="Доллары в выпадающем списке"
    )

    placeholder_summ = BaseLocator(
        selector="#mapDashboardFilters >> [type='text']",
        description="Поле ввода суммы для снятия средств"
   )

    input_summ = BaseLocator(
        selector="200",
        description="Сумма для снятия средств"
    )

    choosing_bank = BaseLocator(
        selector=".PartnerFilters__partnerName_Xpeyb:has-text('Т-Банк')",
        description="Выбор Т-Банк в списке банков"
    )