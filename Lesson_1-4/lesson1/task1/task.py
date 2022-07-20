def task1(number: int) -> int:
    # todo пиши тут свое решение
    number = str(number)
    n_1 = int(number[0])
    n_2 = int(number[:2])
    n = int(number)
    number=n+n_1+n_2
    return number
