def task4(n: int) -> list:
    # todo пиши тут свое решение
    a = []
    for i in range(1, n+1):
        if i%5 ==0:
            a.append(i)
    return a
