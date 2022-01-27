import time
from fonctions import *

def KeyGen(k) : 
    p = genNum(k)
    q = genNum(k)
    while (q == p):     # p et q différents
        q = genNum(k)
    
    N = p*q
    phiN = (p-1)*(q-1)

    e = choseEps(phiN)
    d = inverse_mod(e, phiN)

    """
    print("p = " + str(p))
    print("q = " + str(q))
    print("N = " + str(N))
    print("PhiN = " + str(phiN))
    print("e = " + str(e))
    print("d = " + str(d))
    """

    return ((N,e),(N,d))
    
    
def E(m,e,N) :
    return exp(m,e,N)

def D(c,d,N) :
    return exp(c,d,N)

def main():
    bitSize = ''
    while type(bitSize) != int:
        bitSize = input("Size of p and q in bits (8 - ~50): \n")
        try:
            bitSize = int(bitSize)
        except:
            pass

    print("Generating keys ...")
    start = time.time()
    pk, sk = KeyGen(bitSize)
    stop = time.time()
    print("Keys generated in " + str(int(stop - start)) + " seconds\n")
    c = ""
    while c != "4":
        c = input("Enter choice :\n1 : Encrypt\n2 : Decrypt\n3 : Display keys\n4 : Exit\n")
        
        # Encrypt
        if c == "1":
            msg = ""
            while type(msg) != int:
                msg = input("Enter message to encrypt (numbers only)\n")
                try:
                    msg = int(msg)
                except:
                    pass
            msg_e = E(msg, pk[1], pk[0])
            print("Encrypted message : " + str(msg_e))
            
        # Decrypt
        elif c == "2":
            msg = ""
            while type(msg) != int:
                msg = input("Enter message to decrypt (numbers only)\n")
                try:
                    msg = int(msg)
                except:
                    pass
            msg_d = E(msg, sk[1], sk[0])
            print("Decrypted message : " + str(msg_d))
        
        # Display
        elif c == "3":
            print("Public key (N, e) : " + str(pk[0]) + ", " + str(pk[1]))
            print("Secret key (N, d) : " + str(sk[0]) + ", " + str(sk[1]))
        print("\n")



if __name__ == "__main__":
    main()