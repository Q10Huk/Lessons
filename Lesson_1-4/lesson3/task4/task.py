def task4() -> int:
    # todo пиши тут свое решение
    z=0
    for i in range(1000000):
        q=str(i)
        q.zfill(6)
        a=q[:3]
        b=q[3:]
        c=[int(x) for x in list(a)]
        d=[int(x) for x in list(b)]
        if sum(c) == sum(d):
            z+=1
    return z
