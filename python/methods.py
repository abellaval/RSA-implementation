import random
import secrets
import math


"""
INVERSE MODULO
"""
#ok pour 16 bits pour p et q
def findInvNaive(e, phiN):
    for i in range(2, phiN):
        if ((e * i)% phiN) == 1:
            return i


def findInvBezout(e, phiN):
    a = phiN
    b = e
    prev = [1,0]
    curr = [0,1]
    
    while b != 0:
        q = a//b
        r = a%b
        x = prev[0] - curr[0] * q
        y = prev[1] - curr[1] * q
        a = b
        b = r
        prev[0] = curr[0]
        prev[1] = curr[1]
        curr[0] = x
        curr[1] = y
    return prev[1]


"""
TEST PRIMALITE
"""
def isPrime(num):
    sqroot = int(math.sqrt(num))
    for i in range(2, sqroot + 1):
        if (num % i) == 0:
            return 0
    return 1


"""
GENERATION NB PREMIER
"""
def genRandom(bitsSize):
    return secrets.randbits(bitsSize)
    #return random.getrandbits(bitsSize)


def genNum(bitsSize):
    prime = False
    generatedNum = 0

    while not prime:
        generatedNum = genRandom(bitsSize)
        prime = isPrime(generatedNum)
    return generatedNum


"""
"""
def pgcdEuclide(a, b):
    first = max(a,b)
    second = min(a,b)
    
    while second != 0:
        tmp = a
        first = second
        second = tmp%second

    return first
def choseEps(phiN):
    if (phiN > 257 and pgcdEuclide(phiN, 257)):
        return 257
    if (phiN > 65537 and pgcdEuclide(phiN, 65537)):
        return 65537
    for i in range(3, phiN):
        if pgcdEuclide(phiN, i) == 1:
            return i