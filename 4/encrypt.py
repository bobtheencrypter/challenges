#!/usr/bin/env python3

# Bob the Encrypter, Bob's Encrypting Corp. August 2024 
# Copyright (C) 2024 Bob the Encrypter.

def encrypt(data):
  encrypted = ""

  for i, j in enumerate(data):
    if i % 2 == 0:
      encrypted += chr(j - 1)
    else:
      encrypted += chr(j + 1)

  return encrypted

def main():
  input_filename = input("enter input filename: ")
  data = open(input_filename, 'rb').read()
  output_filename = input("enter output filename: ")
  encrypted = encrypt(data)

  open(output_filename, 'w').write(encrypted)

if __name__ == "__main__":
  main()
