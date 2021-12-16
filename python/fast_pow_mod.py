def fast_pow_mod(b, e, m):
    mask = 1
    res = 1
    b_pow2n = b
    while True: # n + 1/2 loop
        if (mask & e) == mask:
            res = (res * b_pow2) % m
        if mask >= e:
            return res
        b_pow2 = (b_pow2 * b_pow2) % m
        mask <<= 1


b = 42
e = 1000000000000000000000
m = 423141234
x = fast_pow_mod(3, 3, m)
# y = pow(b, e, m)
print(x)
# print(y)
