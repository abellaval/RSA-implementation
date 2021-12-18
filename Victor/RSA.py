"""
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
"""

import secrets


# Fichier fonctions
def pgcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def euclide(a: int, n: int) -> (int, int, int):
    """
    Extended euclide algorithm
    Source: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    :rtype: (gcd, bizout_coeff_1, bizout_coeff_2)
    """
    s, old_s = 0, 1
    r, old_r = n, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    return old_r, old_s, (old_r - old_s * a) // n if n != 0 else 0


def inverse_mod(x: int, p: int) -> int:
    """
    retourne l'inverse de x modulo p,
    c'est-à-dire l'entier y dans [1,p-1] tel que
    xy = 1 mod p

    Attention : il peut y avoir des erreurs dans la suite si
    on ne force pas y à être positif, il faut donc vraiment retourner
    y dans [1,p-1].
    """
    y = 1
    while (x * y) % p != 1:
        y += 1
    return y


def is_prime(n):
    """
    Un test de primalité naïf (voir slides de présentation sur Teams)
    Vous pourrez cette fonction par une implémentation de l'algo de
    Miller-Rabin, à terme

    Implementation: Miller's deterministic test for n < 2^64
    :params n: n > 1 and odd
    Source: https://en.wikipedia.org/wiki/Miller–Rabin_primality_test
    """
    if n <= 1:
        return False

    d = n - 1
    r = 0
    while not (d & 0b1):  # is even
        d >>= 1
        r += 1
    # sufficient for n < 2^64
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)  # x = a ** d % n, uses fast expo internally
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:  # for..else, else block is executed if the loop is not broken
            return False
    return True


def exp(a: int, x: int, p: int) -> int:
    """
    Calcule a^x mod p
    avec la méthode de l'exponentiation rapide
    """
    # builtin already uses fast expo for ints
    # the C implementation will always be faster than any python impl
    # return pow(a, x, p)
    # But for study purpose

    res = 1
    a = a % p
    if a == 0:
        return 0
    while x > 0:
        if x & 0b1:
            res = (res * a) % p
        x >>= 1
        a = (a * a) % p
    return res


# Fichier main
def KeyGen(k):
    """
    Génère des celfs RSA à partir de deux nombres premiers p et q,
    chacun étant des entiers de k-bits.
    Le module N est donc un entier d'neviron 2k-bits.
    Par souci de simplicité, on peut poser directement e = 65537,
    à condition évidemment que phi = (p-1)(q-1) soit plus petit que e.

    int --> ((int,int),(int,int))
    
    Input : Le paramètre de sécurité k
    Output : Le tuple ((N,e),(N,d)) représentant les clefs
    """
    e = (1 << 16) + 1
    p, q = 0, 0
    while not is_prime(p):
        # the | 0b1 forces odd result and avoids 0,
        # we lose 2 as potential prime,
        # but it is bad for security anyway
        p = secrets.randbits(k) | 0b1
    while not is_prime(q):
        q = secrets.randbits(k) | 0b1
    phi = (p - 1) * (q - 1)
    gcd, _, d = euclide(phi, e)
    while phi > e or gcd != 1:
        while not is_prime(p):
            p = secrets.randbits(k) | 0b1
        while not is_prime(q):
            q = secrets.randbits(k) | 0b1
        phi = (p - 1) * (q - 1)
        gcd, _, d = euclide(phi, e)
    N = p * q
    return (N, e), (N, d)


def E(m, e, N):
    """
    Chiffre un message m avec la clef publique PK = (N,e).
    m et le chiffré rendu en sortie doivent être des entiers,
    on ne convertit rien en texte, ici.

    int,int,int --> int

    Input : Un message m ; l'exposant e ; le module N
    Output : Un chiffré c
    """
    return pow(m, e, N)


def D(c, d, N):
    """
    Déchiffre un chiffré c avec la clef privée SK = (N,d).
    c et le message rendu en sortie doivent être des entiers,
    on ne convertit rien en texte, ici.

    int,int,int --> int

    Input : Un chiffré c ; l'exposant d ; le module N
    Output : Un message m
    """
    return pow(c, d, N)

# TODO: Code is untested.
