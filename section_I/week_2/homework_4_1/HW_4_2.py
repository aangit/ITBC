#Write functions that take two lists as arguments and return a list representing the intersection/difference of those lists.

#Example for difference:
# List1 = [10, 20, 30, 40]
# List2 = [10, 30, 50, 70]
# Output_list = [20, 40, 50, 70]

# #Example for intersection:
# List1 = [10, 20, 30, 40]
# List2 = [10, 30, 50, 70]
# Output_list = [10, 30]

def find_diff(list1, list2):
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    for j in list2:
        if j not in list1:
            list3.append(j)
    return list3


def find_intersection(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            list3.append(i)
    return list3


list1 = [10, 20, 30, 40]
list2 = [10, 30, 50, 70]

print(find_diff(list1, list2))
print(find_intersection(list1, list2))