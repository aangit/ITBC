# Check if all elements of a tuple are equal.

t1 = (1, 1, 1, 1)

def check_if_equal(t1):
    first_element = t1[0]
    for i in t1[1:]:
        if i!=first_element:
            return False
    return True

print(check_if_equal(t1))