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



# Fichier fonctions
def pgcd(a,b) : 

def euclide(a,n) :

def inverse_mod(x,p)
    """
    retourne l'inverse de x modulo p,
    c'est-à-dire l'entier y dans [1,p-1] tel que
    xy = 1 mod p

    Attention : il peut y avoir des erreurs dans la suite si
    on ne force pas y à être positif, il faut donc vraiment retourner
    y dans [1,p-1].
    """


def is_prime(n) :
    """
    Un test de primalité naïf (voir slides de présentation sur Teams)
    Vous pourrez cette fonction par une implémentation de l'algo de
    Miller-Rabin, à terme
    """


def exp(a,x,p):
    """
    Calcule a^x mod p
    avec la méthode de l'exponentiation rapide
    """

    



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


def E(m,e,N) :
    """
    Chiffre un message m avec la clef publique PK = (N,e).
    m et le chiffré rendu en sortie doivent être des entiers,
    on ne convertit rien en texte, ici.

    int,int,int --> int

    Input : Un message m ; l'exposant e ; le module N
    Output : Un chiffré c
    """

def D(c,d,N) :
    """
    Déchiffre un chiffré c avec la clef privée SK = (N,d).
    c et le message rendu en sortie doivent être des entiers,
    on ne convertit rien en texte, ici.

    int,int,int --> int

    Input : Un chiffré c ; l'exposant d ; le module N
    Output : Un message m
    """  
