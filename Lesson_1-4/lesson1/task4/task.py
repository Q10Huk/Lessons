def task4(string: str) -> (str, int):
    # todo пиши решение тут.
    #  a - английская!
    a = len(string) - len(string.replace('a', ''))
    string = string.replace('a', '')
    return string, a
