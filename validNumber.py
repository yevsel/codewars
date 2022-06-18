def isNumber(s: str) -> bool:
    symbols = "eE"
    numbers = "0123456789"
    signs = "+-"
    l = list(s)
    dot = False
    e = False
    num = False
    for i in range(len(l)):
        if l[i] in numbers:
            return True
        elif l[i] in signs:
            if l[i+1] in numbers:
                return True
            elif l[i+1] in symbols:
                return False
        else:
            if l[i] == '.':
                return True
            elif l[i] in symbols:
                return False


print(isNumber('e'))
