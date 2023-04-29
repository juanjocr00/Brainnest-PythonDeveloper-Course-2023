'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don't know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

import re

def caesar_brute_force(message):
    english = []
    t=0
    for key in range(26):
        decrypted_message = decrypt(message, key)
        print(f"Key {key}: {decrypted_message}")
        if is_english(decrypted_message):
            english.append(key)
            english.append(decrypted_message)
            t = 1
            
    if t==1:
        print(f"The message is: {english[1]} \nKey used:{english[0]}")
    else:
        print("The message did not use the Caesar Cipher")
        
            

def decrypt(message, key):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - key) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - key) % 26 + 97)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def is_english(text):
    common_english_words = ["the", "and", "or", "is", "are", "of", "it", "in", "to"]
    words = re.findall(r'\b\w+\b', text.lower())
    english_word_count = sum(word in common_english_words for word in words)
    return english_word_count >= 1

encrypted_message = input("Enter the encrypted message:\n> ")
caesar_brute_force(encrypted_message)
