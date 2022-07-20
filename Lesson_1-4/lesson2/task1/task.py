def task1(n: int) -> list:
    # todo пиши тут свое решение
    a = []
    for i in range(1, n):
        if i%2 == 0 and i%3 == 0:
            a.append(i)
    return a
