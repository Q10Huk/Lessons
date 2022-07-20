def task7(string: str) -> str:
    # todo пиши тут свое решение
    import os.path
    string = os.path.splitext(string)
    string = string[0].split('\\')
    return string[-1]
