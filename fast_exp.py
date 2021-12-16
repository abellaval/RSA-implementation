def getBiggest2Pow(x):
    res = 1
    while True:
        n = res << 1
        if (n > x):
            return res
        res = n

def fast_mod_pow(b, e, n):
    mask = getBiggest2Pow(e)
    res = b
    while mask > 1:
        mask = mask >> 1
        res = (res * res) % n
        if (mask & e) == mask:
            res = (res * b) % n
    return res


b = 42
e = 1000000000000000000000
m = 423141234
x = fast_mod_pow(b, e, m)
# x = pow(b, e, m)
print(x)
