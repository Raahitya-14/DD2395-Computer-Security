3#!/usr/bin/env python3
from insecure_hash import hash_string
from Crypto.Cipher import AES


def find_collision(message):
    key= "raahirandomkey12"
    hash_Val=hash_string(message)
    cipher= AES.new(key)
    res= cipher.encrypt(hash_Val)
    res= res + key.encode()
    return res


if __name__ == '__main__':
    message = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb".encode()
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))