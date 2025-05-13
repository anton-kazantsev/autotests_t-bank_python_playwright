from locators.base_locator import BaseLocator


class FinancialManagementLocator:

    container_fin_management = BaseLocator(
        selector='[data-test="independent-parent-iframe"] iframe',
        description='Плейсхолдер'
    )