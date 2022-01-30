#!/usr/bin/env python3

import translator
import argparse

parser = argparse.ArgumentParser(prog='pycode64')
parser.add_argument('--en', help='Encode to base64.')
parser.add_argument('--de', help='Decode to UTF-8.')
args = parser.parse_args()

def writer(text):
    final_file = open(f'{filename[:-4]}.new', 'w')
    final_file.writelines(text)
    final_file.close()
    print(f'new file has been written to {filename[:-4]}.new')
if args.en:
    filename = args.en
    print('encoding...')
    new_file = translator.encoder(args.en)
    writer(new_file)
elif args.de:
    filename = args.de
    print('decoding...')
    new_file = translator.decoder(args.de)
    writer(new_file)


