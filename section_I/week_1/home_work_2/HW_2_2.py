#Write a program to calculate and print the bill at a pizzeria. Each order contains only one pizza.

#The pizza can be in sizes S (500 RSD), M (650 RSD), or L (770 RSD).
#Each bill also includes a delivery fee. The delivery fee is 109 RSD. In case the weather conditions are bad 
#(expressed with a probability of 35%), an additional amount of 50 RSD is included.

#If the total bill amount exceeds 800 RSD, the delivery fee is reduced by 20% 
#(this reduction does not apply to the extra charge for bad weather conditions).
#Note: Use the random() function to implement probability.

import random

S = 500
M = 650
L = 770
delivery_fee = 109
total_bill = 0
choice = "Yes"

while choice != "No":
    pizza_size = input("What size of pizza do you want? S/M/L: ")

    if pizza_size == "S":
        total_bill += S
    elif pizza_size == "M":
        total_bill += M
    elif pizza_size == "L":
        total_bill += L
    else:
        print("Invalid pizza size entered")
        continue

    choice = input("Do you want to place another order? Choose Yes or No: ")
    while choice != "Yes" and choice != "No":
        choice = input("Do you want to place another order? Choose Yes or No: ")

probability = random.random()
if probability < 0.35:
    total_bill += 50

if total_bill + delivery_fee > 800:
    delivery_fee *= 0.8
total_bill += delivery_fee

print(f"The bill is: {total_bill}")