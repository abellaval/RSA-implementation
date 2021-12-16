def fast_pow_mod(b, e, m):
    mask = 1
    res = 1
    l_val = b
    while mask <= e:
        if (mask & e) == mask:
            res = (res * l_val) % m
        l_val = (l_val * l_val) % m
        mask <<= 1
    return res


b = 42
e = 1000000000000000000000
m = 423141234
x = fast_pow_mod(b, e, m)
# y = pow(b, e, m)
print(x)
# print(y)
