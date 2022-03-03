from math import *
from random import randint as rand



def exp(x,e,N) :
    '''
    Calcule x**e mod N avec l'exponentiation rapide
    '''
    res = 1
    while True :
        if e & 1:
            res = (res * x) % N
        if e == 1:
            return res
        x = (x * x) % N
        e >>= 1



def naive_is_prime(n):
    if n < 2 : return False
    if n == 2 : return True
    
    for i in range(2, int(sqrt(n))+1) :
        if n%i == 0 : return False
    return True

def euclide(a, b, u0=1, v0=0, u1=0, v1=1):

    if b == 1 : return (u1,v1)
    return euclide(b, a%b, u1, v1, u0-u1*(a//b), v0-v1*(a//b))     
    


def inverse(x,n) :
    '''
    Inverse de x mod n
    '''
    return euclide(x,n)[0]



def int_str(n):
    '''
    Transforme un entier en chaine de charactère. L'entier DOIT contenir un-multiple-de-6 bits
    Format : chaque symbole (a-z, A-Z, 0-9, espace et virgule) est codé sur 6bits.
    a-z --> 0-25
    A-Z --> 26-51
    0-9 --> 52-61
    espace --> 62
    virgule --> 63
    '''

    b = bin(n)[2:]
    while len(b)%6 != 0 : b = '0'+b
    char = [b[6*i:6*i+6] for i in range(len(b)//6)]
    char = [int(k,2) for k in char]
    char.reverse()

    string = ''
    for c in char :
        if 0 <= c <= 25 :
            string += chr(c+97)
        elif 26 <= c <= 51 :
            string += chr(c-26+65)
        elif 52 <= c <= 61 :
            string += chr(c-52+48)
        elif c == 62 :
            string += ' '
        elif c == 63 :
            string += ','

            
    return string


def str_int(s):

    n = 0
    indice = 0
    for char in s :
        if 97 <= ord(char) <= 122 :
            value = ord(char)-97
        elif 65 <= ord(char) <= 90 :
            value = ord(char)-65+26
        elif 48 <= ord(char) <= 57 :
            value = ord(char)-48+52
        elif ord(char) == 32:
            value = 62
        elif ord(char) == 44:
            value = 63  

        n += value*((2**6)**indice)
        indice +=1
    return n
        
    
