def task3(n: int) -> list:
    # todo пиши тут свое решение
    a = []
    col = 0
    for i in range(2, n):
        for g in range(1, n):
            if i%g == 0:
                col +=1
        if col == 2:
            a.append(i)
            col = 0
        else:
            col = 0
    return a
