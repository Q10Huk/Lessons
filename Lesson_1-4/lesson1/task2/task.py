def task2(number: int) -> int:
    # todo пиши тут свое решение
    number = str(number)[0:]
    number = ' '.join(number)
    number = number.split()
    number = [int(number) for number in number]
    number = sum(number)
    return number