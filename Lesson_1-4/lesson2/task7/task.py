def task7(wish_list: list) -> list:
    # todo пиши тут свое решение
    from operator import itemgetter
    wish_list.sort(key=lambda x: x['Цена'], reverse=True)
    return wish_list[:2]
