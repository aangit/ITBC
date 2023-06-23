# Find all lists in the list whose sum of elements is greater than 45 and display them. 
# [[11,14,1], [33, 2], [33,33,4], [8, 19, 15]]

lists = [[11,14,1], [33, 2], [33,33,4], [8, 19, 15]]

for i in lists:
    sums = 0
    for j in i:
        sums = sums+j
    if sums > 45:
        print(i)