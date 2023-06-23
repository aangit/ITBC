# Write a love calculator that works like this:
# The user enters two full names and surnames of the person whose "love compatibility" is calculated
# First, count the number of occurrences of all letters from the words 'TRUE' and 'LOVE' for each person.
# Then you need to combine (concatenate) the value obtained for the person whose name and surname is first 
# in alphabetical order with the value obtained for the second person.
# If the value obtained is:
# Between 40 and 50, a message should be displayed: "Your score is XX, there will be a wedding!"
# Less than 10 or more than 90: "You are like Mentos and Cola!"

first_person = input("Insert your first name and your last name: ")
second_person = input("Insert your partner's first name and last name: ")

value_to_check = "trueloveTRUELOVE"

counter_1 = 0
for i in first_person:
    if i in value_to_check:
        counter_1+=1

counter_2 = 0
for i in second_person:
    if i in value_to_check:
        counter_2+=1

love_score = str(counter_1)+str(counter_2)

if int(love_score) >=40 and int(love_score) <=50:
    print(f"your score is {love_score} , expect wedding!")
elif int(love_score) <=10 and int(love_score) >=90:
    print(f"Your score is {love_score} , you are like mint and coke")
else:
    print(f"Your score is {love_score}")

    


