#Write a program that accepts two numbers (N and M) as input. 
#It displays N numbers from the Fibonacci sequence whose values are greater than M. 
#If any of the generated numbers is equal to M, it immediately stops further display. 
#Note: Use the break statement at the appropriate place in the program.

def find_fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return find_fibonacci(number-1) + find_fibonacci(number-2)
   

n = int(input("Insert the first number"))
m = int(input("Insert the second number"))
for i in range(1,n):
    if find_fibonacci(i) != m:
        print(find_fibonacci(i))
    else:
        break
       