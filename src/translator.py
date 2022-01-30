#!/usr/bin/env python3

import base64

def encoder(response):
    if response.endswith(".txt"):
        f = open(response, 'r')
        response = f.read()
    output = base64.b64encode(response.encode())
    output = output.decode() # removes b'...'
    return output

def decoder(response):
    if response.endswith(".txt"):
        f = open(response, 'r')
        response = f.read()
    output = base64.b64decode(response)
    output = output.decode() # removes b'...'
    return output
