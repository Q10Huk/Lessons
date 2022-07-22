from atf.ui import *


class MainPage(Region):
    """Главная страница"""

    news = CustomList(By.CSS_SELECTOR, '.controlls-Surggest_list .controls-ListView__itemV', 'Новости')
    search = TextField(By.CSS_SELECTOR, '[name="header"] input', 'Поиск')

    def search_and_open_news(self, news_name):
        """
        Ищем и открываем новсть
        :param news_name: Название новости"""

        self.search.type_in(news_name)
        self.news.item(contains_text=news_name).click()

    def check_text_by_title(self, title_news, text_news):
        """
        Проверка текста новости по заголовку
        :param title_news: Заголовок новости
        :param text_news: Текст новости"""

        self.search.type_in(title_news)
        self.news.item(contains_text=text_news).should_be(ContainsText(text_news))
