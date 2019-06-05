#!/usr/bin/python
#-*- coding: UTF-8 -*-
"""
                author: karmenshu@jlq.com
"""


import base64
import ssl
import struct
import sys

from Crypto.Hash import SHA256
from binascii import b2a_hex, a2b_hex


if __name__ == '__main__':

#        if len(sys.argv) != 9:
#                print 'Usage: ' + sys.argv[0] + ' Bootstrap/Secure_Monitor/TEE_OS/Bootloader/Linux_Kernel/TL <source_image> <dest_addr> \
#<pubkey_file>/null <privkey_file>/null LK/CK/null <aeskey_file>/null anti_rollback/null'
#                exit(1)

        data = '0123456789ABCDEF'

        digest = SHA256.new(data)
        print 'SHA256 of image data: ', digest.hexdigest()
        print 'SHA256 of image data: ', digest.digest()

        print 'the result should be :2125b2c332b1113aae9bfc5e9f7e3b4c91d828cb942c2df1eeb02502eccae9e9'
