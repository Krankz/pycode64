#!/usr/bin/env python3

import base64
from sys import argv

i = 0
# when running as binary, change index 
if argv[0] != 'python3':
    i = 1

def encoder(response):
    if response.endswith(".txt"):
        f = open(response, 'r')
        response = f.read()
    output = base64.b64encode(response.encode())
    output = output.decode() # removes b'...'
    print(output)

def decoder(response):
    if response.endswith(".txt"):
        f = open(response, 'r')
        response = f.read()
    output = base64.b64decode(response)
    output = output.decode() # removes b'...'
    print(output)

if argv[i] == '-e':
    print('encoding...')
    encoder(argv[i+1])
elif argv[i] == '-d':
    print('decoding...')
    decoder(argv[i+1])
