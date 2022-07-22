from atf import *
from atf.ui import *
from Lessons.Lesson_6.pages.auth_page import AuthPage
from Lessons.Lesson_6.pages.main_page import MainPage
from Lessons.Lesson_6.pages.notes_page import NotePage




class TestNameSuite(TestCaseUI):

    @classmethod
    def setUpClass(cls):           # Выполняется 1 раз перед всеми тестами в классе (н-р, авторизация в ЛК)
        cls.browser.open('https://fix-online.sbis.ru/auth/')
        AuthPage(cls.driver).auth('testoootest', 'Qwerty123')

    def setUp(self):                # Выполняется перед каждым тестом
        NotePage(self.driver).search.should_be(Displayed, wait_time=True)

    # def test_01_name_test(self):    # Непосредственно тесты. Обязателен префикс "test_"
    #     MainPage(self.driver).search_and_open_news('Новость для автотеста')
    #
    # def test_02_name_test(self):    # И так далее, но не очень много
    #     MainPage(self.driver).check_text_by_title(title_news='Новость для автотеста',
    #                                               text_news='не удаляйте')

    def test_open_notes(self):
        NotePage(self.driver).notes_click()

    def tearDown(self):             # Выполняется после каждого теста
        self.browser.close_windows_and_alert()

    @classmethod
    def tearDownClass(cls):        # Выполняется 1 раз после всех тестов в классе
        pass

# if __name__ == '__main__':
#     run_tests()                       # Запуск тестов

