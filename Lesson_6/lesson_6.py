from atf.ui import *
import item

class AuthPage(Region):
    """Страница авторизации"""

    login = Element(By.CSS_SELECTOR, '[name="login"]', 'Логин')
    password = Element(By.CSS_SELECTOR, '[name="password"]', 'Пароль')
    enter_btn = Element(By.CSS_SELECTOR, '.auth-Form__submit', 'Войти')

    def auth(self, user_login, user_password):
        """
        Авторизация пользователя
        :param user_login: Логин
        :param user_password: Пароль
        :return:
        """
        self.login.type_in(user_login)
        self.password.type_in(user_password)
        self.enter_btn.click()

# class CustomList(Element):
#     """
#     Класс для работы с разнообразными списками.
#     Для того, чтобы задать список в locators нужно указать локатор,
#     по которому будут находиться все элементы списка
#     """
#
#     def __str__(self) -> str:
#         return 'произвольный список'
#
#     def item(self, item_number: int = 0, with_text: str = '', contains_text: str = '',
#              contains_text_ignoring_case: str='', match_regex: Any = None, element_type: Type = None) -> 'Element':
#         """Возвращает экземпляр класса Item или Control"""
#         pass

