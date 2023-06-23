# Pronaci najveci element u listi i prikazati ga. 


def find_largest_nr(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
 
list = [4, 6, 9, 13, 0]
 
print(find_largest_nr(list))