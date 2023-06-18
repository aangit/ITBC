# Write a function that takes two lists as input and creates a new list containing the even elements from the first list 
# and the odd elements from the second list. Sort the elements in descending order.

def find_even(list1):
    list3 = []
    for i in list1:
        if i % 2 == 0:
            list3.append(i)
    return list3


def find_odd(list2):
    list3 = []
    for i in list2:
        if i % 2 != 0:
            list3.append(i)
    return list3


def sorting(input_list):
    for k in range(0, len(input_list)-1):
        for l in range(k + 1, len(input_list)):
            if(input_list[k] < input_list[l]):
                x = input_list[k]
                input_list[k] = input_list[l]
                input_list[l] = x
    return input_list


list1 = [2, 1, 66, 4, 3, 87, ]
list2 = [4, 4, 6, 99, 34, 3, 7, 10, -2, -10]

filtered_list = find_even(list1) + find_odd(list2)
final_list = sorting(filtered_list)
print(final_list)