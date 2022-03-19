from time import time
from .miller_rabin import *


def random(k):
    """
    Génère un entier de k-bits exactement
    """

    n = 2 ** (k - 1)
    for i in range(k - 1):
        n += rand(0, 1) * (2 ** i)
    return n


def KeyGen(k):
    """
    Le module RSA N est de longueur k bits
    """

    t1 = time()
    (p, q) = (0, 0)

    while not miller_rabin(p):
        p = random(k // 2)
    while not miller_rabin(q):
        q = random(k // 2)

    if p == q: return None

    N = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, phi) != 1:
        e = rand(3, phi - 1)

    d = inverse(e, phi)
    if d < 0: d += phi

    t2 = time()
    return ((e, N), (d, N), p, q, phi, int(t2 - t1))


def E(M, e, N):
    return exp(M, e, N)


def D(C, d, N):
    return exp(C, d, N)


def Encrypt(m, e, N):
    if len(m) > int(log(N, 2) / 6) + 1:
        print(f'message trop long : {len(m)} caractères')
        return None
    tmp = int_str(E(str_int(m), e, N))
    tmp = tmp.replace(' ', '$')
    tmp = tmp.replace(',', '&')
    return tmp


def Decrypt(c, d, N):
    c = c.replace('$', ' ')
    c = c.replace('&', ',')
    return int_str(D(str_int(c), d, N))


global N, e, d, p, q, phi, t


def show(N, e, d, p, q, phi):
    print('-' * 20)
    print('>>> p = ', p)
    print('>>> q = ', q)
    print('>>> N = ', N)
    print('>>> phi = ', phi)
    print('-' * 20)
    print()


def display_help():
    print('-' * 20)
    print('Authorized characters : a-z, A-Z, 0-9, space and comma')
    print('-' * 20)
    print()


def main():
    k = int(input("Security parameter (size of N in bits) : "))
    ((e, N), (d, N), p, q, phi, t) = KeyGen(k)

    print(
        f"{'-' * 20}\nN : {int(log(N, 2)) + 1}-bits\nlog(N)/6 : {int(log(N, 2) / 6) + 1} caractères maximum par message\nGénération des clefs : {t} secondes\n{'-' * 20}\n\n")

    while True:
        mode = input(
            "Enter e/d/q/s/h for encryption/decryption/quit/show-keys/help : ")
        if mode.upper() == 'Q':
            return None
        if mode.upper() == 'S':
            show(N, e, d, p, q, phi)
        if mode.upper() == 'H':
            display_help()
        if (mode.upper() != 'E') and (mode.upper() != 'D'):
            continue
        text = input("Enter plain/cipher to encrypt/decrypt : ")
        if mode.upper() == 'E':
            print("{}\n>>> Plaintext : {}\n>>> Ciphertext : {}\n{}\n".format(
                '-' * 20, text, Encrypt(text, e, N), '-' * 20))
        if mode.upper() == 'D':
            print("{}\n>>> Ciphertext : {}\n>>> Plaintext : {}\n{}\n".format(
                '-' * 20, text, Decrypt(text, d, N), '-' * 20))


if __name__ == "__main__":

    if 1:
        main()  # Génération des clefs et ersatz d'UI
    else:
        k = 32
        ((e, N), (d, N), p, q, phi, t) = KeyGen(
            k)  # Generation des clefs et c'est tout
