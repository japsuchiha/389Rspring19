#!/usr/bin/env python3

import hashlib
import string

def crack():
    hashes = open("hashes.txt") # open and read hashes.txt
    passwords = open("passwords.txt") # open and read passwords.txt
    characters = string.ascii_lowercase

    hash = hashes.read().split('\n')
    # print(hash)
    for p in passwords:
        for c in characters:
            # crack hashes
            x = hashlib.sha256()
            # print(x)
            x.update(bytes((c+p).rstrip(),'ascii'))

            if x.hexdigest() in hash:
                print("{}:{}".format((c+p).rstrip(),x.hexdigest()))
            

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52

if __name__ == "__main__":
    crack()
