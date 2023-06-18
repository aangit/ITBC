# Write a function that iterates through a list and checks if all elements within the list are of the same type. 
# If they are, the function returns True; otherwise, it returns False.

def check_if_true(n):
    for i in n:
        if not isinstance(i, type(list[0])):
            return False
    return True

list = [1, 2, []]

print(check_if_true(list))
