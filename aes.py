#!/usr/bin/python
#-*- coding: UTF-8 -*-
"""
        @author shuli27749@gmail.com
"""


import base64
import ssl
import struct
import sys

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class AES_CIPHER:
        def __init__(self, key):
                self.key = key
                self.mode = AES.MODE_CBC

        def encrypt(self, data):
                encryptor = AES.new(self.key, self.mode,
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                block_size = 16
                remainder = len(data) % block_size
                if remainder != 0:
                        data = data + ('\0' * (block_size - remainder))
                self.crypt_data = encryptor.encrypt(data)
                return self.crypt_data

        def decrypt(self, data):
                decryptor = AES.new(self.key, self.mode,
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                plain_data = decryptor.decrypt(data)
                return plain_data


if __name__ == '__main__':

        data = '1111222233334444'
        key128 = '0123456789ABCDEF'
        key256 = '00112233445566778899AABBCCDDEEFF'

        encryptor128 = AES.new(key128, AES.MODE_ECB)

        block_size = 16
        remainder = len(data) % block_size
        if remainder != 0:
                data = data + ('\0' * (block_size - remainder))
        crypt_data = encryptor128.encrypt(data)

        print'AES128 crypt_data :', crypt_data
        print'AES128 crypt_data :', b2a_hex(crypt_data)

        encryptor256 = AES.new(key256, AES.MODE_ECB)
        crypt_data = encryptor256.encrypt(data)

        print'AES256 crypt_data :', crypt_data
        print'AES128 crypt_data :', b2a_hex(crypt_data)
