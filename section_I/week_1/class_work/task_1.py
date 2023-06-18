#Write a program that checks whether each entered integer is divisible by the sum of its digits. 
#The program will terminate after the user enters 2 such numbers. 
#It will display appropriate messages to the user. Note: Do not use string operations, only number operations.

counter = 0
while counter < 2:
    num = int(input("Please insert your number "))
    result = 0
    temp = num
    while temp!=0:
        digit = temp%10
        result = result + digit
        temp= temp//10
        
    if num%result ==0:
        print("number can be divided")
        counter+=1
    else:
        print("number cannot be divided")

print("Bye")