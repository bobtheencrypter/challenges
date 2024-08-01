#!/usr/bin/env python3

# Bob the Encrypter, Bob's Encrypting Corp. August 2024 
# Copyright (C) 2024 Bob the Encrypter.

import base64

def encrypt(data):
  encrypted = base64.b64encode(data).decode()

  return encrypted

def main():
  input_filename = input("enter input filename: ")
  data = open(input_filename, 'rb').read()
  output_filename = input("enter output filename: ")
  encrypted = encrypt(data)

  open(output_filename, 'w').write(encrypted)

if __name__ == "__main__":
  main()
