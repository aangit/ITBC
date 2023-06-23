# Write a program that accepts one number at a time from the user until the user enters the number 0. 
# Determine the sum of the entered numbers that are divisible by the sum of their digits.
# Write a function to determine whether a number is divisible by the sum of its digits and use it appropriately to solve the problem.

def counting_numbers(inserted):
    result = 0
    total = 0
    temp = inserted
    while temp!=0:
        digit = temp%10
        result = result + digit
        temp=temp//10

    if inserted%result == 0:
        total = total + inserted
        return True
    else:
        return False

print(counting_numbers(12))

number = int(input("Insert your number: "))
while number!=0:
    print(counting_numbers(number))
    number = int(input("Insert your number: "))