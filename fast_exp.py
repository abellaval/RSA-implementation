def getHeavyBit(x):
    res = 1
    while True:
        n = res << 1
        if (n > x):
            return res
        res = n

def fast_mod_pow(b, e, n):
    mask = getHeavyBit(e)
    res = b
    while mask > 1:
        mask = mask >> 1
        res = (res * res) % n
        if (mask & e) == mask:
            res = (res * b) % n
    return res


x = fast_mod_pow(2, 3, 6)
print(x)
