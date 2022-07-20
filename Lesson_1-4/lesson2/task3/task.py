def task3(n: int) -> int:
    # todo пиши тут свое решение
    a = 1
    if n%2 == 0:
        for i in range(2, n+1, 2):
            a *= i
    else:
        for i in range(1, n+1, 2):
            a *= i
    return a

