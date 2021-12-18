import math
import secrets

def pgcd(a,b) : 
    first = max(a,b)
    second = min(a,b)
    
    while second != 0:
        tmp = a
        first = second
        second = tmp%second
    return first


def euclide(a,n) :
    pass


def inverse_mod(x,p):       # renvoie l'inverse de x % p
    a = p
    b = x
    prev = [1,0]    # première ligne
    curr = [0,1]    # deuxième ligne
    
    while b != 0:
        q = a//b
        r = a%b     # reste
        tmp0, tmp1 = prev[0] - curr[0] * q, prev[1] - curr[1] * q
        # a, b -> b, reste
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
            return 0
    return 1


def exp(a,x,p):     # expo rapide
    res = 1
    v = a
    loop = int(math.log2(x)+1)
    for _ in range(loop):
        if x % 2 == 1:
            res = (res * v) % p
        x >>= 1
        v = (v ** 2) % p 
    return res
    


"""
Autres fonctions
"""

def choseEps(phiN):
    if (phiN > 65537 and pgcd(phiN, 65537)):
        return 65537
    for i in range(3, phiN):
        if pgcd(phiN, i) == 1:
            return i


def genRandom(bitsSize):
    return secrets.randbits(bitsSize)


def genNum(bitsSize):
    prime = False
    generatedNum = 0

    while not prime:
        generatedNum = genRandom(bitsSize)
        prime = is_prime(generatedNum)
    return generatedNum