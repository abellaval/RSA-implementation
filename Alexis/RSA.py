'''
Fonctions pour une implémentation basique de RSA.
Devrait permettre de générer des premiers p et q de taille 2^20 (~un million)
et donc N d'environ 40 bits.

Sans l'algorithme d'exponentation rapide,chiffrer/déchiffrer
des messages devient impossible si N dépasse 20 bits.
Avec l'exponentaition rapide, ces opérations sont instantanées
quelle que soit la taille de N. 

Note :
On ne cherche pas une implémentation optimale : le simple usage
des bons algorithmes sera suffisant pour pouvoir utiliser RSA
de manière un peu sérieuse.
'''
from math import sqrt, floor
import random



# Fichier fonctions
def pgcd(a,b) :
    """
    Largest common denominator
    """
    a, b = b, a % b
    while b != 0:
        a, b = b, a % b
    return a


def euclide(a,n) :
    """
    Extended euclide algorithms
    Source: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    """
    s, old_s = 0, 1
    r, old_r = n, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    pgcd = old_r
    bezout_coef = old_s, (old_r - old_s * a) // n if n != 0 else 0
    return pgcd, bezout_coef

def inverse_mod(x,p):
    """
    retourne l'inverse de x modulo p,
    c'est-à-dire l'entier y dans [1,p-1] tel que
    xy = 1 mod p

    Attention : il peut y avoir des erreurs dans la suite si
    on ne force pas y à être positif, il faut donc vraiment retourner
    y dans [1,p-1].

    Hypothesis: x and p are co-prime
    """
    y = euclide(x, p)[1][0]
    while y < 1:
        y += p
    return y


def is_prime(n) :
    """
    Un test de primalité naïf (voir slides de présentation sur Teams)
    Vous pourrez cette fonction par une implémentation de l'algo de
    Miller-Rabin, à terme
    """
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i != 0:
            return False
    return True


def exp(a,x,p):
    """
    Calcule a^x mod p
    avec la méthode de l'exponentiation rapide
    """
    a = a % p
    if a == 0: return 0
    result = 1
    while x:
        if x & 1:
            result = (result * a) % p
        x >>=1 # Div by 2 bitwise
        a = (a * a) % p
    return result




# Fichier main
def KeyGen(k) : 
    """
    Génère des celfs RSA à partir de deux nombres premiers p et q,
    chacun étant des entiers de k-bits.
    Le module N est donc un entier d'neviron 2k-bits.
    Par souci de simplicité, on peut poser directement e = 65537,
    à condition évidemment que phi = (p-1)(q-1) soit plus petit que e.

    int --> ((int,int),(int),(int))
    
    Input : Le paramètre de sécurité k
    Output : Le tuple ((N,e),(N,d)) représentant les clefs
    """
    e = 65537
    p = random.getrandbits(k)
    q = random.getrandbits(k)
    N = p*q
    while not is_prime(p):
        p = random.getrandbits(k)
    while not is_prime(q) and p != q:
        q = random.getrandbits(k)

    phiN = (p - 1) * (q - 1)
    if phiN >= e:
        find_eps(phiN)
    d = inverse_mod(e, phiN)
    return (N, e), (N, d)


def find_eps(phiN):
    """
    Find epsilon co-prime with phiN
    """
    res = random.randint(3, phiN)
    while pgcd(res, phiN) != 1:
        res = random.randint(3, phiN)
    return res


def E(m,e,N) :
    """
    Chiffre un message m avec la clef publique PK = (N,e).
    m et le chiffré rendu en sortie doivent être des entiers,
    on ne convertit rien en texte, ici.

    int,int,int --> int

    Input : Un message m ; l'exposant e ; le module N
    Output : Un chiffré c
    """
    return exp(m, e, N)

def D(c,d,N) :
    """
    Déchiffre un chiffré c avec la clef privée SK = (N,d).
    c et le message rendu en sortie doivent être des entiers,
    on ne convertit rien en texte, ici.

    int,int,int --> int

    Input : Un chiffré c ; l'exposant d ; le module N
    Output : Un message m
    """
    return exp(c, d, N)

if __name__ == "__main__":
    from sys import argv
    print(KeyGen(int(argv[1])))
