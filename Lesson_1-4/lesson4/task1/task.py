import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

def change_month(date: str, count: int) -> None:
    # todo пиши тут свое решение
    """
    :param date: дата в формате dd.mm.yy
    :param count: количество месяцев
    :return: дата в формате dd.mm.yy
    """
    date = datetime.strptime(date, '%d.%m.%y').date()
    date = (date + relativedelta(months=+count)).isoformat()
    date = date.split('-')
    date[0] = date[0][2:]
    date = date[::-1]
    date = '.'.join(date)
    return date
