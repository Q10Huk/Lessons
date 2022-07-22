from atf.ui import *

import time


class NotePage(Region):
    """Страница Заметки"""
    documents = Element(By.CSS_SELECTOR, '[name="item-documents"]', 'Документы')
    documents_notes = Element(By.CSS_SELECTOR, '[href="/page/notes"]', 'Заметки')

    def notes_click(self):
        """Переход в раздел Документы/Заметки"""
        self.documents.click()
        time.sleep(1)
        self.documents_notes.click()
        time.sleep(2)

    # def notes_new(self):
    #     """Создание новой заметки"""
    #     pass