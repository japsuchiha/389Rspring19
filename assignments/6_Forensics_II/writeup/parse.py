#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

magic, version = struct.unpack("<LL", data[0:8])
timestamp = datetime.datetime.utcfromtimestamp(int(struct.unpack("<L", data[8:12])[0]))).isoformat()
author = ''.join(struct.unpack("<8s", data[12:20])))
section_count = int(struct.unpack("<L", data[20:24])[0])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

if section_count <= 0:
    bork("Bad section count! Got %d, expected a positive value" % section_count)

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" % timestamp)
print("AUTHOR: %s" % author)
print("SECTION: %d" % section_count)

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
SECTION_ASCII = 0x1
SECTION_UTF8 = 0x2
SECTION_WORDS = 0x3
SECTION_DWORDS = 0x4
SECTION_DOUBLES = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_PNG = 0x8
SECTION_GIF87 = 0x9
SECTION_GIF89 = 0xA

elem = data[24:]
pos = 0

for section in range(1,section_count+1):
    sec_type = hex(struct.unpack("<L", body[pos:(pos+4)])[0])
    sec_len = int(struct.unpack("<L", body[(pos+4):pos+8])[0])
    pos = pos+8

    print("SECTION: %d" % (section_count))
    print("TYPE: %s" % sec_type)
    print("LENGTH: %d" % sec_len)


    if sec_type == hex(SECTION_ASCII):
        print("VALUE: %s\n" % (struct.unpack(("<%ds" % sec_len), elem[(pos):(pos+sec_len)]))[0])

    elif sec_type == hex(SECTION_UTF8):
        print("  VALUE: %s\n" % (struct.unpack(("<%ds" % sec_len), elem[(pos):(pos+sec_len)])).decode('utf-8')[0])

    elif sec_type == hex(SECTION_WORDS):
        words = sec_len / 4
        print("  VALUE: %s\n" % (struct.unpack(("<%s" % 'L'*words), elem[(pos):(pos+sec_len)]))[0])

    elif sec_type == hex(SECTION_DWORDS):
        dwords = sec_len / 8
        print("  VALUE: %s\n" % (struct.unpack(("<%s" % 'Q'*dwords), elem[(pos):(pos+sec_len)]))[0])

    elif sec_type == hex(SECTION_DOUBLES):
        doubles = sec_len / 8
        print("  VALUE: %s\n" % (struct.unpack(("<%s" % 'd'*doubles), elem[(pos):(pos+sec_len)]))[0])

    elif sec_type == hex(SECTION_COORD):
        if sec_len != 16:
            bork("Bad coordinate size in section %d! Expected size 16, but was %d" % (sec_count, slen))
        print("COORDINATES: %s\n" % (struct.unpack("<dd", elem[(pos):(pos+sec_len)]),))

    elif sec_type == hex(SECTION_REFERENCE):
        if sec_len != 4:
            bork("Bad reference! Expected size 4, but was %d" % sec_len)
        print("REFERENCE: %d\n" % int(struct.unpack("<L", elem[(pos):(pos+sec_len)])[0]))

    elif sec_type == hex(SECTION_PNG):
        signature = [137, 80, 78, 71, 13, 10, 26, 10]
        png = (signature + list(struct.unpack('<' + ("%s" % 'B'*sec_len), elem[(pos):(pos+sec_len)])))
        newPic = open("newPic.png", "wb")
        newPic.write(bytearray(png))

        print("\n")

    elif sec_type == hex(SECTION_GIF87):
        signature = [47, 49, 46, 38, 37, 61]
        png = (signature + list(struct.unpack('<' + ("%s" % 'B'*sec_len), elem[(pos):(pos+sec_len)])))
        newGif = open("newGif87.gif", "wb")
        newGif.write(bytearray(png))

        print("\n")

    elif sec_type == hex(SECTION_GIF89):
        signature = [47, 49, 46, 38, 39, 61]
        png = (signature + list(struct.unpack('<' + ("%s" % 'B'*sec_len), elem[(pos):(pos+sec_len)])))
        newGif = open("newGif89.gif", "wb")
        newGif.write(bytearray(png))

        print("\n")
    
    pos = pos + sec_len