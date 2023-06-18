#Write a program for encrypting and decrypting messages. 
#At the beginning, the user enters a message and a key (an integer reference value in the range of 1 to 5) to be used in the process. 
#Then the user chooses an operation by entering the word "encrypt" or "decrypt". 
#The program displays the processed message as output.

def encrypt(message, key):
    """
    It takes a message and a key, and returns the message encrypted with the key
    
    :param message: The message to be encrypted
    :param key: The key is the number of characters to shift the message by
    :return: The result of the encryption.
    """
    result = ''
    for i in range(0, len(message)):
        result = result + chr(ord(message[i]) + int(key))
    return result


def decrypt(message, key):
    """
    It takes a message and a key, and returns the message decrypted using the key
    
    :param message: The message to be encrypted
    :param key: The key is the number of characters to shift the message by
    :return: The result of the decryption.
    """
    result = ''
    for i in range(0, len(message)):
        result = result + chr(ord(message[i]) - int(key))
    return result


choice1 = ""
while choice1!="encrypt" and choice1!="decrypt":
    choice1 = input("If you want to encrypt the message type encrypt, or otherwise, type decrypt: ")

if choice1 == "encrypt":
    key = input("Enter counter from 1 to 5 ")
    while key not in ["1","2","3","4","5"]:
        key = (input("Enter counter from 1 to 5 "))
    message = input("Insert your message ")
    res = encrypt(message, key)
    print(res)
else:
    key = input("Enter counter from 1 to 5 ")
    while key not in ["1","2","3","4","5"]:
        key = input("Enter counter from 1 to 5 ")
    message = input("Insert your message ")
    res1 = decrypt(message, key)
    print(res1)