# Write a program that inserts an element X before each element of a list.

nums = [4, 7, 3, 4, 6, 2]

unique_list=[]
for i in nums:
    el="x"
    unique_list.append(i)
    unique_list.append(el)
print(unique_list)