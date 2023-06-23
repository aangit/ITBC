# Find the index of the smallest element in the list, then print all the elements after that index.

list1=[2,5,3,4,1,6,7]

mini = 999
for i in list1:
    if i<mini:
        mini = i
a=list1.index(mini)
print(list1[a+1:])