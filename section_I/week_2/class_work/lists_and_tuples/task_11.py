# Sum the elements of 2 tuples so that the elements of one tuple are added to the elements at the corresponding index
# of the other tuple. 
# Example: (1,2,3) and (3,3,5), resulting tuples: (4, 5, 8)

t1 = (1,2,3)
t2 = (3,3,5)

list_1 = list(t1)
list_2 = list(t2)

list_3 = []
for i in range(0, len(list_1)):
    list_3.append(list_1[i] + list_2[i])
print (list_3)
