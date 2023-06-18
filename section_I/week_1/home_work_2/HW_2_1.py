#Write a program that determines, for each entered integer, whether the entered number contains more even or odd digits. 
#Terminate the input after the user enters a number that has all digits even or all digits odd. 
#Note: Do not use operations on strings, but rather on numbers!

even_counter = - 1
odd_counter = - 1

digit = 0

while even_counter!= 0 and odd_counter != 0:

    number = int(input('Insert number '))
    even_counter = 0
    odd_counter = 0
    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
        number = number//10

    if even_counter==0 or odd_counter==0:
        break

    if even_counter > odd_counter:
        print('There are more even digits')
    elif even_counter == odd_counter:
        print('Equal number of even and odd digits')
    else:
        print('There are more odd digits')

print('Invalid input, end of the program')

