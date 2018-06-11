#!/usr/bin/env python

import sys, string


def caesar(plaintextfile, ciphertextfile, shiftkey):
    lower_alpha = string.ascii_lowercase
    lower_shift = lower_alpha[shiftkey:] + lower_alpha[:shiftkey]
    upper_alpha = string.ascii_uppercase
    upper_shift = upper_alpha[shiftkey:] + upper_alpha[:shiftkey]
    mapping = string.maketrans(lower_alpha + upper_alpha, lower_shift + upper_shift)
    with open(plaintextfile, 'r') as p:
        plain = p.read()
    p.close()
    with open(ciphertextfile + '.txt', 'w') as p:
        p.write(plain.translate(mapping))
    p.close()
    pass


def usage():
    print "Usage:"
    print "encrypt <plaintext file> <output ciphertext file>"
    print "decrypt <ciphertext file> <output plaintext file>"
    sys.exit(1)


if len(sys.argv) != 4:
    usage()
elif sys.argv[1] == 'encrypt':
    caesar(sys.argv[2], sys.argv[3], 5)
elif sys.argv[1] == 'decrypt':
    caesar(sys.argv[2], sys.argv[3], -5)
else:
    usage()
