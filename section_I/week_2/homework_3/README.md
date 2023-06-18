## Find Prime Divisors Program

The find prime divisors program is designed to find and display the prime divisors of a given number. It performs the following steps:

1. Define a function called `divisors` that searches for prime divisors of a given number.
2. Iterate through numbers from 2 to the given number.
3. Check if each number is a divisor of the given number and if it is prime.
4. If the number is both a divisor and prime, add it to the list of prime divisors.
5. Return the list of prime divisors from the function.

### Usage

1. Run the program.
2. Enter a number for which you want to find the prime divisors.
3. The program will display the prime divisors of the entered number.


# Encryption and Decryption Program

This program provides functionality for encrypting and decrypting messages using a key. It also includes a program for finding the prime divisors of a given number.

## Encryption and Decryption Program

The encryption and decryption program allows users to input a message and a key, and then choose between encryption or decryption operations. The program performs the following actions:

- **Encryption**: Each character in the message is shifted forward in the Unicode table by a specific number of values based on the entered key.
- **Decryption**: It is the inverse operation of encryption. Each character in the message is shifted backward in the Unicode table by the same number of values based on the entered key.

### Usage

1. Run the program.
2. Enter a message.
3. Enter a key, which should be an integer value in the range of 1 to 5.
4. Choose either "encrypt" or "decrypt" operation.
5. The program will display the processed message.

**Note:** The encryption process shifted each character in the message forward by 3 positions in the Unicode table.
