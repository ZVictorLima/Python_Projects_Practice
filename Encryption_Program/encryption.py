# This will be a substitution cipher encryption project

  

import random

import string # This is a module that contains all the letters of the alphabet

  

chars = string.punctuation + string.digits + string.ascii_letters + " " # This is a string that contains all the characters that can be encrypted

  
  

chars = list(chars) # This converts the string into a list now we can use the random.shuffle() function to shuffle the characters

key = chars.copy() # This creates a copy of the list so that the original list is not changed

# print(f"Original list: {chars}")

# print(f"Key: {key}")

  

random.shuffle(key) # This shuffles the key list

# print(f"Shuffled key: {key}")

  

# The idea is to replace each character in the text with the corresponding character in the key

def encrypt(text, key):

    encrypted_text = ""

    for char in text:

        index = chars.index(char)

        encrypted_text += key[index]

    print(f"Encrypted text: {encrypted_text}")

    return encrypted_text

  

def decrypt(text, key):

    decrypted_text = ""

    for char in text:

        index = key.index(char)

        decrypted_text += chars[index]

    print(f"Decrypted text: {decrypted_text}")

    return decrypted_text

  

plain_text = input("Enter the text you want to encrypt: ")

cypher_text = encrypt(plain_text, key)

decrypt(cypher_text, key)