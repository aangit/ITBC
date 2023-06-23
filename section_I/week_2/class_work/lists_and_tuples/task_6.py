# Find the unique values in the list and display them. 
# Those that occur only once in a given list are unique. [22, 18, 10, 1, 3, 7, 10, 3, 18]

list_1 = [22, 18, 10, 1, 3, 7, 10, 3, 18]

list_2 = []
counts = {}
for i in list_1:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1

for count in counts:
    if counts[count] == 1:
        list_2.append(count)

print(list_2)       