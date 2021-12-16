from methods import *

def genKey():
    bitsSize = ''  
    # loop while input is not correct
    while type(bitsSize) != int:
        bitsSize = input("Enter bits size of N (fast up to 64) : \n")
        try:
            bitsSize = int(bitsSize)
        except:
            pass

    # Generate prime numbers p and q
    p = genNum(bitsSize//2)
    q = genNum(bitsSize//2)

    # N and phiN
    N = p*q
    phiN = (p-1)*(q-1)

    # e prime with phiN
    e = choseEps(phiN)

    d = findInvBezout(e, phiN)
    while d < 0:
        d += phiN


    #"""    
    print("p = " + str(p))
    print("q = " + str(q))
    print("N = " + str(N))
    print("phiN = " + str(phiN))
    print("e = " + str(e))
    print("d = " + str(d))
    #"""

    return (N,e,d)


if __name__ == "__main__":
    N, e, d = genKey()