def task6(number_list: list) -> (int, int):
    # todo пиши тут свое решение
    a = 0
    b = 1
    for i in number_list:
        a += i
        b *= i
    return a, b
