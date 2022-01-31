import math
import secrets

def pgcd(a,b) : 
    first = max(a,b)
    second = min(a,b)
    while second != 0:
        first, second = second, first%second
    return first


def euclide(a,n) :
    prev = [1,0]
    curr = [0,1]
    while n != 0:
        q = a//n
        r = a%n
        prev, curr = [curr[0], curr[1]], [prev[0] - curr[0] * q, prev[1] - curr[1] * q]
        a, n = n, r
    return a, prev[0], prev[1]  # pgcd, coeff a, coeff n


def inverse_mod(x,p):       # renvoie l'inverse de x % p
    
    res = euclide(x, p) # res[1] qui nous intéresse
    inv = res[1]
    while inv < 0:  # valeur retournée bien positive
        inv += p
    return inv % p


def is_prime(n):
    sqroot = int(math.sqrt(n))
    for i in range(2, sqroot + 1):
        if (n % i) == 0:
            return False
    return True

def temoin_miller(n, rand):
    # n - 1 = 2**s * d
    # représentation binaire de n-1 = d + s bits à 0
    
    d = n-1
    s = 0
    while (d%2) != 1:
        d = d // 2
        s += 1
    
    x = exp(rand, d, n)
    if (x == 1) or (x == n-1):
        return False
    for _ in range(s-1):
        x = exp(x,2,n)
        if (x == n - 1):
            return False
    return True 


def miller_rabin(n, k):     # n : nbr à tester, k : nbr d'itérations
    tested = []
    for _ in range(k):
        rand = secrets.randbelow(n-4) + 2
        while (rand in tested):
            rand = secrets.randbelow(n-4) + 2
        tested.append(rand)
        if temoin_miller(n, rand):
            return False
    return True


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
    if (phiN > 65537 and euclide(phiN, 65537)[0] == 1):
        return 65537
    
    for i in range(3, euclide(phiN, i)[0] == 1):
        if pgcd(phiN, i) == 1:
            return i


def genNum(bitsSize):
    prime = False
    while not prime:
        generatedNum = secrets.randbits(bitsSize)
        prime = (generatedNum%2 == 1) and miller_rabin(generatedNum, 20)
        #prime = is_prime(generatedNum)
    return generatedNum