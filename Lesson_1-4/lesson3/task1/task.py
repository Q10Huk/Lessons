def cash(deposit: int, percent: int, years: int) -> int:
    # todo пиши тут свое решение
    return round(deposit*((1+percent/100)**years))
