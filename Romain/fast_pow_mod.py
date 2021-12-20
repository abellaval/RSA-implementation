def fast_pow_mod(b, e, m):
    res = 1
    while True: # n + 1/2 loop
        if e & 1:
            res = (res * b) % m
        if e==0:
            return res
        b = (b * b) % m
        e >>= 1


b = 42
e = 1000000000000000000000
m = 423141234
x = fast_pow_mod(2, 6, m)
# y = pow(b, e, m)
print(x)
# print(y)
