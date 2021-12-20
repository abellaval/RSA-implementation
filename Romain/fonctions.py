import math
import secrets

def pgcd(a,b) : 
    first = max(a,b)
    second = min(a,b)
    while second != 0:
        first, second = second, first%second
    return first


def euclide(a,n) :
    pass


def inverse_mod(x,p):       # renvoie l'inverse de x % p
    a = p
    b = x
    prev = [1,0]    # première ligne
    curr = [0,1]    # deuxième ligne
    while b != 0:
        q = a//b    # quotient
        r = a%b     # reste
        tmp0, tmp1 = prev[0] - curr[0] * q, prev[1] - curr[1] * q
        a, b = b, r
        # passe à la ligne suivante
        prev[0], prev[1] = curr[0], curr[1]
        curr[0], curr[1] = tmp0, tmp1

    while prev[1] < 0:  # valeur retournée bien positive
        prev[1] += p
    return prev[1] % p


def is_prime(n) :
    sqroot = int(math.sqrt(n))
    for i in range(2, sqroot + 1):
        if (n % i) == 0:
            return False
    return True


def exp(a,x,p):     # expo rapide
    res = 1
    while True : // n + 1/2 loop
        if e & 1:
            res = (res * b) % m
        if e == 1:
            return res
        b = (b * b) % m
        e >>= 1

"""
Autres fonctions
"""

def choseEps(phiN):
    if (phiN > 65537 and pgcd(phiN, 65537)):
        return 65537
    for i in range(3, phiN):
        if pgcd(phiN, i) == 1:
            return i


def genNum(bitsSize):
    prime = False
    while not prime:
        generatedNum = secrets.randbits(bitsSize)
        prime = is_prime(generatedNum)
    return generatedNum