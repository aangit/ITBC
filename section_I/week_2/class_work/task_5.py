# Write a program in which the user enters sentence by sentence until "end" is entered. 
# Write a function to determine the number of lowercase or uppercase letters in the given text.
# Using this function, determine the number of entered sentences in which the number of uppercase letters
# is an integer divisor of the number of lowercase letters.

from curses.ascii import isupper


def find_lower_case_and_upper_case(word):
    counter_1 = 0
    counter_2 = 0
    for i in word:
        if i.isupper():
            counter_1+=1
        elif i.islower():
            counter_2+=1
    return counter_1, counter_2


sentence_count = 0
is_end = False
while not is_end:
    sentence = input("Insert your sentence: ")
    if sentence!="End":
        counter1, counter2 = find_lower_case_and_upper_case(sentence)
        print(counter1, counter2)
        if counter1 >0 and counter2> 0: 
            if counter1 % counter2 == 0:
                sentence_count+=1
    else:
        is_end = True
print(f"Total number is: {sentence_count}")
            