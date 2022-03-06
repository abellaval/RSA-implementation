from math import *
from random import randint as rand
from website.crypto.tools import *


def miller_rabin(n, k=40):
    """
    Test de Miller-Rabin avec probabilité 2^-k
    """

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    s, t = 0, n - 1
    while t % 2 == 0:
        s += 1
        t //= 2

    for _ in range(k):
        a = rand(2, n - 1)
        x = exp(a, t, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = exp(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
