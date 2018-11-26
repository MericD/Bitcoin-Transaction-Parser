from hashlib import *
from base58 import *

def SHA256D(bstr):
    return sha256(sha256(bstr).digest()).digest()

def ConvertPKHToAddress(prefix, addr):
    data = prefix + addr
    return b58encode(data + SHA256D(data)[:4])

def PubkeyToAddress(pubkey_hex):
    pubkey = bytearray.fromhex(pubkey_hex)
    round1 = sha256(pubkey).digest()
    h = new('ripemd160')
    h.update(round1)
    pubkey_hash = h.digest()
    return ConvertPKHToAddress(b'\x00', pubkey_hash)

#pubkey_hex="8C02DE9B92890517CC3C0F379C68386069260D8D2D72CCBF79F601B86194D43B"

#print(PubkeyToAddress(pubkey_hex))

def cluster_senderAdd(pubkey_hex, arrhex):
    for i in pubkey_hex:
        for j in arrhex:
            if i in j:
                j = i + j
                #j = list(set(i + j)) 
    return arrhex


