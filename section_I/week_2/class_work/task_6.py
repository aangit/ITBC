# Write a program that, for each entered number, displays the divisors of that number on the output, which are also prime. 
# The input stops when the user enters the number 0.

import math

def divisors(num):
    result=[]
    for i in range(1,num//2 +1):
        if num%i ==0:
            result.append(i)
    result.append(num)
    return result

def is_prime(num):
    sroot=int(math.sqrt(num))
    for i in range(2,sroot + 1):
        if (num%i) == 0:
            return False
    return True

num = -1
while num!=0:
    while True:
        try:
            num = int(input("Insert your number "))
            break
        except ValueError:
            print("please enter a valid choice")

    div_result = divisors(num)
    prime_result = is_prime(num)
    all_together =[]
    for i in div_result:
        if is_prime(i):
            all_together.append(i)
    if num ==0:
        break
    print(all_together)
print("That's all folks")
