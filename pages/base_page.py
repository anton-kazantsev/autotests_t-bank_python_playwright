from playwright.sync_api import Page, Response, expect, Locator
from data import base_data
from typing import Optional, Any


expect.set_options(timeout=30000)
class BasePage:

    combobox = 'combobox'
    option = 'option'
    link = 'link'
    button = "button"
    textbox = 'textbox'
    checkbox = 'checkbox'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url: str = base_data.base_url

    def open(self, uri: str) -> Optional[Response]:
        """
        Переход на конкретную страницу сайта
        """
        return self.page.goto(f"{self.base_url}{uri}")

    def fill_placeholder(self, loc: str, name: str, fill: str) -> Any:
        """
        Заполнение плейсхолдера
        """
        return self.page.locator(loc).content_frame.get_by_role("textbox", name=name).fill(fill)

    def checkbox_uncheck(self, loc: str, name: str) -> Any:
        """
        Нажатие на чекбокс
        """
        return self.page.locator(loc).content_frame.get_by_role("checkbox", name=name).uncheck()

    def choice_locator(self,
                       locator: Optional[str] = None,
                       role = None,
                       name: Optional[str] = None,
                       title: Optional[str] = None,
                       text: Optional[str] = None,
                       test_id: Optional[str] = None,
                       label: Optional[str] = None
                       ) -> Locator:
        """
        Выбор типа локатора:
        """
        if locator is not None:
            return self.page.locator(locator)
        elif role is not None:
            return self.page.get_by_role(role, name=name)
        elif title is not None:
            return self.page.get_by_title(title)
        elif text is not None:
            return self.page.get_by_text(text)
        elif test_id is not None:
            return self.page.get_by_test_id(test_id)
        elif label is not None:
            return self.page.get_by_label(label)
        else:
            raise ValueError(
                "Необходимо передать одно из значений для выбора необходимого типа возвращаемого локатора: "
                "locator, role+name, title, text, test_id или label."
            )


    def click_choice_locator(self,
                             locator: Optional[str] = None,
                             role: Optional[str] = None,
                             name: Optional[str] = None,
                             title: Optional[str] = None,
                             text: Optional[str] = None,
                             test_id: Optional[str] = None,
                             label: Optional[str] = None
                             ) -> Any:
        """
        Клик на выбранный локатор
        """
        return self.choice_locator(locator, role, name, title, text, test_id, label).click()


    def fill_choice_locator(self,
                            fill: str,
                            locator: Optional[str] = None,
                            role: Optional[str] = None,
                            name: Optional[str] = None,
                            title: Optional[str] = None,
                            text: Optional[str] = None,
                            test_id: Optional[str] = None,
                            label: Optional[str] = None
                            ) -> Any:
        """
        Заполнение плейсхолдеда
        """
        return self.choice_locator(locator, role, name, title, text, test_id, label).fill(fill)


    def hover_choice_locator(self,
                             locator: Optional[str] = None,
                             role: Optional[str] = None,
                             name: Optional[str] = None,
                             title: Optional[str] = None,
                             text: Optional[str] = None,
                             test_id: Optional[str] = None,
                             label: Optional[str] = None
                             ) -> Any:
        """
        Наведение на выбранный локатор
        """
        return self.choice_locator(locator, role, name, title, text, test_id, label).hover()


    def checkbox_uncheck_choice_locator(self,
                                        locator: Optional[str] = None,
                                        role: Optional[str] = None,
                                        name: Optional[str] = None,
                                        title: Optional[str] = None,
                                        text: Optional[str] = None,
                                        test_id: Optional[str] = None,
                                        label: Optional[str] = None
                                        ) -> Any:
        """
        Снятие чекбокса внутри локатора
        """
        return self.choice_locator(locator, role, name, title, text, test_id, label).uncheck()


    def expect_to_visible_choice_locator(self,
                                         locator: Optional[str] = None,
                                         role: Optional[str] = None,
                                         name: Optional[str] = None,
                                         title: Optional[str] = None,
                                         text: Optional[str] = None,
                                         test_id: Optional[str] = None,
                                         label: Optional[str] = None
                                         ) -> None:
        """
        Ожидание отображения локатора
        """
        return expect(self.choice_locator(locator, role, name, title, text, test_id, label)).to_be_visible()


    def open_new_page_after_click_choice_locator(self,
                                                 locator: Optional[str] = None,
                                                 role: Optional[str] = None,
                                                 name: Optional[str] = None,
                                                 title: Optional[str] = None,
                                                 text: Optional[str] = None,
                                                 test_id: Optional[str] = None,
                                                 label: Optional[str] = None
                                                 ) -> Page:
        """
        Клик на локатор и открытие новой вкладки
        """
        with self.page.expect_popup() as popup_info:
            self.choice_locator(locator, role, name, title, text, test_id, label).click()
        new_page = popup_info.value
        return new_page