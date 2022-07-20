class Name:
    """Класс для работы с ФИО"""

    def __init__(self, FIO):
        self.FIO = FIO
        if self._check():
            self.F = FIO.split()[0]
            self.I = FIO.split()[1]
            if len(self.FIO.split()) == 3:
                self.O = FIO.split()[2]
        pass

    def _check(self):
        """
        Проверка правильности переданого формат ФИО
        :return:
        """
        if len(self.FIO.split()) == 2 or len(self.FIO.split()) == 3:
            return True
        else:
            return False

    # @property
    def strfname(self, str_format):
        """Преобразует переданный формат в строку
        %Ф - фамилия, %ф - первая буква фамилии
        %И - имя, %и - первая буква имени
        %О - отчество, %о - первая буква отчества
        """
        if str_format == '%Ф %И %О':
            return self.F + ' ' + self.I + ' ' + self.O
        if str_format == '%И %О %ф.':
            return self.I + ' ' + self.O + ' ' + self.F[0] + '.'
        if str_format == '%и.%ф.':
            return self.I[0] + '.' + self.F[0] + '.'
        if str_format == '%и.%ф.%о.':
            return self.I[0] + '.' + self.F[0] + '.' + self.O[0] + '.'
        if str_format == '%Ф %и. %о.':
            return self.F + ' ' + self.I[0] + '. ' + self.O[0] + '.'



    @property
    def brief_name(self):
        """Сокращенное имя (без отчества)
        :return: Возвращает строку вида Петров Иван
        """
        return self.F + ' ' + self.I

    @property
    def initials(self):
        """Инициалы
        :return: Возвращает строку вида Петров И.С.
        """
        if len(self.FIO.split()) == 2:
            return self.F + ' ' + self.I[0] + '.'
        else:
            return self.F + ' ' + self.I[0] + '.' + self.O[0] + '.'

FIO = Name('Федоров Антон Вованович')