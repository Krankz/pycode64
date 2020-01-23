import base64
from sys import argv

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

if argv[1] == '-e':
    print('encoding...')
    encoder(argv[2])
elif argv[1] == '-d':
    print('decoding...')
    decoder(argv[2])
