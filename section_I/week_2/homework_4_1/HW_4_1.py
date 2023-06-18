#Write a function that generates sublists from a given list.
#Example:
#List = [10, 20, 30, 40]
#Sublist = [[], [10], [20], [30], [40], [10, 20], [10, 30], ... [10, 20, 30, 40]]

import itertools


def findsubsets(s, n):
    return list(itertools.combinations(s, n))


def find_list_subsets(lista):
    result = []
    for i in range(0, len(lista)+1):
        sub_list = findsubsets(lista, i)
        result = result + sub_list
    return result


def convert_tuple_into_list(lista):
    list_of_list = []
    for i in lista:
        list_of_list.append(list(i))
    return list_of_list

lista = [10, 20, 30, 40]
print(convert_tuple_into_list(find_list_subsets(lista)))