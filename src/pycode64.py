#!/usr/bin/env python3

import translator
import argparse

parser = argparse.ArgumentParser(prog='pycode64')
parser.add_argument('--en', help='Encode to base64.')
parser.add_argument('--de', help='Decode to UTF-8.')
args = parser.parse_args()

if args.en:
    print('encoding...')
    translator.encoder(args.en)
elif args.de:
    print('decoding...')
    translator.decoder(args.de)


