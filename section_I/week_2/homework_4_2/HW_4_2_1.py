# Write a function that will display all subsets of a given set.

# Example:
# Input: {1, 2, 3}
# Output: {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}

import itertools
 
 
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
 
 
def find_set_subsets(lista):
    result = []
    for i in range(0, len(lista)+1):
        sub_list = findsubsets(lista, i)
        result = result + sub_list
    return result
 
 
 
def convert_tuple_into_set(lista):
    list_of_list = []
    for i in lista:
        list_of_list.append(set(i))
    return list_of_list
 
 
input_set = {1, 2, 3}
set_list = convert_tuple_into_set(find_set_subsets(input_set))
print(set_list)