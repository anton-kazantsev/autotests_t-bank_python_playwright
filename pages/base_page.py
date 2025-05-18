from playwright.sync_api import Page, Response, expect
from data import base_data
from typing import Optional


expect.set_options(timeout=30000)
class BasePage:

    combobox = 'combobox'
    option = 'option'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url: str = base_data.base_url

    def open(self, uri: str) -> Optional[Response]:
        """
        Переход на конкретную страницу сайта
        """
        return self.page.goto(f"{self.base_url}{uri}")

    def click_locator(self, loc):
        """
        Клик на локатор
        """
        return self.page.locator(loc).click()

    def expect_locator(self, loc):
        """
        Ожидание локатора
        """
        return expect(self.page.locator(loc)).to_be_visible()

    def fill_placeholder(self, loc, name, fill):
        """
        Заполнение плейсхолдера
        """
        return self.page.locator(loc).content_frame.get_by_role("textbox", name=name).fill(fill)

    def checkbox_uncheck(self, loc, name):
        """
        Нажатие на чекбокс
        """
        return self.page.locator(loc).content_frame.get_by_role("checkbox", name=name).uncheck()

    def click_by_role_link(self, sort, name):
        """
        Клик на элемент по роли
        """
        return self.page.get_by_role(sort, name=name).click()

    def click_by_title(self, title):
        """
        Клик по элементу с нужным тайтлом
        """
        return self.page.get_by_title(title).click()

    def open_new_page(self, title):
        """
        Клик на тайтл и открытие новой вкладки
        """
        with self.page.expect_popup() as popup_info:
            self.page.get_by_title(title).click()
        new_page = popup_info.value
        return new_page

    def open_new_page_after_click_by_role(self, sort, name):
        """
        Клик на роль и открытие новой страницы
        """
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role(sort, name=name).click()
        new_page = popup_info.value
        return new_page

    def fill_placeholder_by_role(self, role, fill, name = None):
        """
        Ввод текста в плейсхолдер
        """
        return self.page.get_by_role(role, name=name).fill(fill)

    def hover_on_element(self, name, role=None):
        """
        Наведение на элемент
        """
        return self.by_locator(name, role).hover()

    # Функция выбора типа локатора
    def by_locator(self, name, role=None):
        """
        Выбор типа передаваемого локатора
        """
        if role is None:
            return self.page.locator(name)
        else:
            return self.page.get_by_role(role, name=name)

    def click(self, name, role=None):
        """
        Клик на локатор
        """
        return self.by_locator(name, role).click()

    def fill_locator(self, name, fill):
        return self.page.locator(name).fill(fill)



    def choice_locator(self,
                       locator=None,
                       role=None, name=None,
                       title=None,
                       text=None,
                       test_id=None,
                       label=None
                       ):
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
                             locator=None,
                             role=None, name=None,
                             title=None,
                             text=None,
                             test_id=None,
                             label=None
                             ):
        """
        Клик на выбранный локатор
        """
        return self.choice_locator(locator, role, name, title, text, test_id, label).click()


    def fill_choice_locator(self,
                            fill,
                            locator=None,
                            role=None, name=None,
                            title=None,
                            text=None,
                            test_id=None,
                            label=None
                            ):
        """
        Заполнение плейсхолдеда
        """
        return self.choice_locator(locator, role, name, title, text, test_id, label).fill(fill)


    def hover_choice_locator(self,
                             locator=None,
                             role=None, name=None,
                             title=None,
                             text=None,
                             test_id=None,
                             label=None
                             ):
        """
        Наведение на выбранный локатор
        """
        return self.choice_locator(locator, role, name, title, text, test_id, label).hover()


    def checkbox_uncheck_choice_locator(self,
                                        locator=None,
                                        role=None, name=None,
                                        title=None,
                                        text=None,
                                        test_id=None,
                                        label=None
                                        ):
        """
        Снятие чекбокса внутри локатора
        """
        return self.choice_locator(locator, role, name, title, text, test_id, label).uncheck()


    def expect_to_visible_choice_locator(self,
                              locator=None,
                              role=None, name=None,
                              title=None,
                              text=None,
                              test_id=None,
                              label=None
                              ):
        """
        Ожидание отображения локатора
        """
        return expect(self.choice_locator(locator, role, name, title, text, test_id, label)).to_be_visible()


    def open_new_page_after_click_choice_locator(self,
                                                 locator=None,
                                                 role=None, name=None,
                                                 title=None,
                                                 text=None,
                                                 test_id=None,
                                                 label=None):
        """
        Клик на локатор и открытие новой вкладки
        """
        with self.page.expect_popup() as popup_info:
            self.choice_locator(locator, role, name, title, text, test_id, label).click()
        new_page = popup_info.value
        return new_page