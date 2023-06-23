# Remove an empty tuple from the list of tuples. Example list: [(1,2), (), (“A”, “B”), (“X”), (), ()]

list_1= [(1,2), (), ("A", "B"), ("X"), (), ()]

while () in list_1:
    list_1.remove(())
print(list_1)