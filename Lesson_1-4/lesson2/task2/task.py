def task2(n: int) -> list:
    # todo пиши тут свое решение
    b = []
    for i in range(n):
        b.append(str(i+1) + ' ' + '*' * (i+1))
    return b
