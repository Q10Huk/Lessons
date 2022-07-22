from atf.ui import *


class AuthPage(Region):
    """Страница авторизации"""

    login = Element(By.CSS_SELECTOR, '[name="Login"]', 'Логин')
    password = Element(By.CSS_SELECTOR, '[name="Password"]', 'Пароль')
    enter_btn = Element(By.CSS_SELECTOR, '[class="auth-AdaptiveLoginForm__loginButtonImage controls-BaseButton__icon controls-icon controls-icon_size-m controls-icon_style-contrast"]', "Войти")

    def auth(self, user_login, user_password):
        """
        Авторизация пользователя
        :param user_login: Логин
        :param user_password: Пароль
        :return:
        """
        self.login.type_in(user_login)
        self.enter_btn.click()
        self.password.type_in(user_password)
        self.enter_btn.click()
