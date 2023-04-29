'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''
def caesar_cipher():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ")
        if choice.lower() == 'e':
            key = int(input("Please enter the key (0 to 25) to use.\n> "))
            message = input("Enter the message to encrypt.\n> ")
            encrypted_message = encrypt(message, key)
            print("Encrypted message:", encrypted_message)
        elif choice.lower() == 'd':
            key = int(input("Please enter the key (0 to 25) to use.\n> "))
            message = input("Enter the message to decrypt.\n> ")
            decrypted_message = decrypt(message, key)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please try again.")

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

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

caesar_cipher()

