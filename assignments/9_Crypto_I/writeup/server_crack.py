
import hashlib
import string
import socket
import time
import re
import pdb
import select


def server_crack():
    hashes = [line.strip() for line in open("hashes.txt", "r")] # open and read hashes.txt
    passwords = [line.strip() for line in open("passwords.txt", "r")] # open and read passwords.txt
    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    hash = {}

    for c in characters:
        for p in passwords:
            code = (c + p).encode()
            res = hashlib.sha256(code).hexdigest()
            hash[res] = code

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    count = 0

    # crack 3 times
    while (count < 3):
        s.setblocking(0)
        ready = select.select([s], [], [], 0.5)
        if ready[0]:
            data = s.recv(1024)
            ans = data.decode().split('\n')[2]
            print(ans)
            print(hash[ans])
            s.send(hash[ans])
            time.sleep(0.3)
            count += 1

    data = s.recv(1024)
    print("flag: {}".format(data))

if __name__ == "__main__":
    server_crack()
