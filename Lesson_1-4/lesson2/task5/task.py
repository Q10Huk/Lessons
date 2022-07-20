def task5(number_list: list) -> list:
    # todo пиши тут свое решение
    a = min(number_list)
    b = max(number_list)
    c = number_list.index(a)
    d = number_list.index(b)
    number_list[c] = b
    number_list[d] = a
    return number_list
