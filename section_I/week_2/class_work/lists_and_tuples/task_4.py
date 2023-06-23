# Write a program that mixes the elements of two lists, 
# where the elements of the second list follow the elements of the first list. 
# If one of the lists has more elements than the other, add the excess elements to the end of the resulting list. 
# Example L1 = [“A”, “Xx”], L2 = [“Y”, 123, 9] ; Result = [“A”, “Y”, “Xx”, 123, 9]



list1=["A","Xx"]
list2=["Y",123,9]

list3 =[]

first = len(list1)
second=len(list2)
if first>second:
    result = first
else:
    result = second

for i in range(0,result):
    if i < len(list1):
        list3.append(list1[i])
    if i <len(list2):
        list3.append(list2[i])
print(list3)
