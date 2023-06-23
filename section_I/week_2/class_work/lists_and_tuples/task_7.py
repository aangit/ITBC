# Sort the list in ascending order. Example output: [1,2,3,4]

list_1 = [3,2,4,1]

for i in range(0, len(list_1)- 1):
    for j in range(i + 1, len(list_1)):
        if list_1[i]>list_1[j]:
            temp = list_1[i]
            list_1[i]= list_1[j]
            list_1[j] = temp

print(list_1)