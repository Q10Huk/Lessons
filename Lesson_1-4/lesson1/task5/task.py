def task5(string: str) -> bool:
    # todo пиши тут свое решение
    string = string.replace('-', '').replace(' ', '').replace('+', '')
    return string.isdigit()