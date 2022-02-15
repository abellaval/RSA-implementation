import hashlib
import os
from typing import Callable
from math import ceil
"""Code inspiré de https://gist.github.com/ppoffice/e10e0a418d5dafdd5efe9495e962d3d2?fbclid=IwAR2i3ufxO0QkH1sIf4brHNAD64MkFEE66x-Htm9287fSTEbEv4-9ecQP-Nc
   et des notations de "PKCS #1: RSA Cryptography Specifications Version 2.2" 
   https://www.rfc-editor.org/rfc/inline-errata/rfc8017.html?fbclid=IwAR0TT8EBxGYUC89UtKxesIqAJjk_4SmVWVkascPkUkPXsrg3w7yKo6xrEfk  
"""
def sha256(m:bytes) -> bytes:
    return hashlib.sha256(m).digest()

def int_to_bytes(x: int) -> bytes:
    """Converts a non negative integer into an octet string """
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def i2osp(integer: int, size) -> bytes:
    """Converts a non negative integer into an octet string of a specified length.
    This is the PKCS #1 I2OSP (Integer-to-Octet-String) primitive"""
    return integer.to_bytes(size,'big')

def mgf1(seed: bytes, maskLen: int, Hash:Callable=sha256) -> bytes:
    """Mask generation function."""
    T = b""
    hLen=len(Hash(T))
    for counter in range(0,ceil(maskLen/hLen)):
        C = i2osp(counter,4)
        T += Hash(seed+C)
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

        
    

def oaep_encode(m:bytes,k:int,label: bytes = b'', Hash:Callable=sha256)->bytes:
    mLen= len(m)
    lhash= Hash(label)
    hLen=len(lhash)
    assert mLen <= k-2*hLen -2 
    ps = b'\x00' * (k- mLen -2*hLen-2)
    DB = lhash+ps+ b'\x01' + m 
    seed = os.urandom(hLen)
    dbMask=mgf1(seed,k-hLen-1,Hash)
    maskedDB = xor(DB,dbMask)
    seedMask= mgf1(maskedDB,hLen)
    maskedSeed = xor(seed,seedMask)
    return b'\x00'+maskedSeed +maskedDB

def oaep_decode(C:bytes,k:int,label:bytes=b'',Hash:Callable=sha256)-> int:
    CLen = len(C)
    assert CLen == k
    lhash = Hash(label)
    hLen = len(lhash)
    assert k >= 2*hLen+2
    maskedSeed= C[1:hLen+1]
    maskedDB=C[hLen+1:]
    seedMask=mgf1(maskedDB,hLen,Hash)
    seed = xor(maskedSeed,seedMask)
    dbMask = mgf1(seed,k-hLen-1,Hash)
    DB = xor(maskedDB,dbMask)
    i = hLen
    while i < len(DB):
        if DB[i] == 0:
            i += 1
            continue
        elif DB[i] == 1:
            i += 1
            break
        else:
            raise Exception()
    m = DB[i:]
    return int.from_bytes(m,'big')
    
if __name__ == "__main__":
    oaep_encode(b'\x00',1)