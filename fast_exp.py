def getBiggest2Pow(x):
    res = 1
    while True:
        n = res << 1
        if (n > x):
            return res
        res = n

def fast_mod_pow(b, e, m):
    mask = getBiggest2Pow(e)
    res = b
    while mask > 1:
        mask = mask >> 1
        res = (res * res) % m
        if (mask & e) == mask:
            res = (res * b) % m
    return res

def fast_mod_pow2(b, e, m):
    mask = 1
    mask_index = 0
    l_index = 0
    l_val = b
    res = 1
    while mask <= e:
        if (mask & e) == mask:
            while l_index < mask_index:
                l_val = (l_val * l_val) % m
                l_index += 1
            res = (res * l_val) % m
        mask_index += 1
        mask = mask << 1
    return res


b = 42
e = 1000000000000000000000
m = 423141234
# x = fast_mod_pow(b, e, m)
# y = fast_mod_pow2(b, e, m)
z = pow(b, e, m)
# print(x)
# print(y)
print(z)
