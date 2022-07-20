def task5(text: str) -> dict:
    # todo пиши тут свое решение
    s = {}
    text = text.replace(',', '').replace('.', '')
    text = text.lower()
    text = text.split()
    for x in text:
        c = text.count(x)
        s[x]=c
    return s
