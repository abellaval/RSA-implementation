def fast_pow_mod(b, e, m):
    mask = 1
    res = 1
    pow2 = b
    while True: # n + 1/2 loop
        if (mask & e) == mask:
            res = (res * pow2) % m
        if (mask >=e):
            return res
        pow2 = (pow2 * pow2) % m
        mask <<= 1


b = 42
e = 1000000000000000000000
m = 423141234
x = fast_pow_mod(3, 3, m)
# y = pow(b, e, m)
print(x)
# print(y)
