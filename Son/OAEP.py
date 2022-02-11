import hashlib
import os
from math import ceil
"""Code inspiré de https://gist.github.com/ppoffice/e10e0a418d5dafdd5efe9495e962d3d2?fbclid=IwAR2i3ufxO0QkH1sIf4brHNAD64MkFEE66x-Htm9287fSTEbEv4-9ecQP-Nc
   et des notations de "PKCS #1: RSA Cryptography Specifications Version 2.2"  
"""
def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def i2osp(integer: int, size) -> bytes:
    """Converts a nonnegative integer into an octet string of a specified length.
    This is the PKCS #1 I2OSP (Integer-to-Octet-String) primitive"""
    return integer.to_bytes(size,'big')

def mgf1(seed: bytes, maskLen: int) -> str:
    """Mask generation function."""
    T = b""
    hLen=32
    for counter in range(0,ceil(maskLen/hLen)):
        C = i2osp(counter,4)
        T += hashlib.sha256(seed+C).digest()
    return T[:maskLen]

def xor(data: bytes, mask: bytes) -> bytes:
    '''Byte-by-byte XOR of two byte arrays'''
    masked = b''
    ldata = len(data)
    lmask = len(mask)
    for i in range(max(ldata, lmask)):
        if i < ldata and i < lmask:
            masked += (data[i] ^ mask[i]).to_bytes(1, byteorder='big')
        elif i < ldata:
            masked += data[i].to_bytes(1, byteorder='big')
        else:
            break
    return masked

        
    

def oaep_encode(m:int,k=int,label=""):
    k0=k1=32
    lhash= hashlib.sha256(label.encode('utf-8')).digest()
    m=int_to_bytes(m)
    mlen= len(m)
    ps = b'\x00' * (k- mlen - k0- k1-2)
    DB = lhash+ps+ b'\x01' + m 
    seed = os.urandom(k0)
    dbMask=mgf1(seed,k-k0-1)
    maskedDB = xor(DB,dbMask)
    seedMask= mgf1(maskedDB,k0)
    maskedSeed = xor(seed,seedMask)
    return b'\x00'+maskedSeed +maskedDB

def oaep_decode(m:bytes,k,label=""):
    maskedSeed= m[1:32+1]
    maskedDB=m[32+1:]
    seedMask=mgf1(maskedDB,32)
    seed = xor(maskedSeed,seedMask)
    dbMask = mgf1(seed,k-32-1)
    DB = xor(maskedDB,dbMask)
    i = 32
    counter=0
    while i < len(DB):
        if DB[i] == 0:
            i += 1
            counter +=1
            continue
        elif DB[i] == 1:
            i += 1
            counter +=1
            break
        else:
            raise Exception()
    m = DB[i:]
    return int.from_bytes(m,'big'),counter
print(oaep_decode(i2osp(134306580035506444299466252429844703797849717368651760821866,25),25))