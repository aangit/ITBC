# Write a program in which the user enters a series of words separated by commas. 
# There may be a space in any part of the input, which should be ignored. On output show:
# The word with the largest and the word with the least number of characters.
# The word with the highest and lowest number of repeated characters.

words = input("Insert words: ")

counter= 0 
for i in words:
    for j in i:
        counter+=1
        if j == " " or j == ",":
            counter-=1
            
print(counter)