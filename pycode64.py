import base64
from sys import argv

def encoder(response):
    output = base64.b64encode(response.encode())
    output = output.decode() # removes b'...'
    print(output)
if argv[1] == '-e':
    print('encoding...')
    encoder(argv[2])
