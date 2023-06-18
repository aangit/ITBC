# inputfile.txt
# Cashier: Milan Jovanovic
# Invoices: 2000, 3330, 9999, 1122.2
# Cashier: Pera Peric
# Invoices: 2999, 3333, 444, 5555
# Cashier: Joca Jovanovic
# Invoices: 3939, 333, 44, 55

# # Read the inputfile.txt and calculate the total revenue generated by each cashier 
# (by summing the values in the Invoices row).
# Create a file for each cashier named firstname_lastname_rank.txt and write the following:
# # Full Name: revenue

# The rank in the output file corresponds to the position based on the earnings
# (the cashier with the highest earnings has rank 1)...

# Sample output:

# Milan_Jovanovic_1.txt:
# Milan Jovanovic: 16451.20
# Pera_Peric_2.txt:
# Pera Peric: 12331.00
# Joca_Jovanovic_3.txt:
# Joca Jovanovic: 4371.00

import json

cashier_dict = {}
with open("inputfile.txt", "r") as reading:
    input_values = True
    values_list = []
    bills_list = []
    while input_values:
        input_values = reading.readlines()
        find_names = input_values[::2]
        find_sale = input_values[1::2]
        for row in find_names:
            values_list.append(row.strip("\n").strip("Kasir:").strip())
        for row in find_sale:
            bills_list.append(row.strip("\n").strip("Racuni:").strip())
    values_list.pop()

    bills_splitted = [i.split(",") for i in bills_list]
    bills = [[float(i) for i in inner] for inner in bills_splitted]
    total_sale = [sum(i) for i in bills]

    for i in range(len(values_list)):
        cashier_dict[values_list[i]] = total_sale[i]

    list_of_dicts = []

    for keys, values in cashier_dict.items():
        fresh_dict = {keys: values}
        list_of_dicts.append(fresh_dict)

    list_of_dicts.sort(key=lambda x: list(x.values())[0], reverse=True)

    for i in list_of_dicts:
        for key, value in i.items():
            with open(f"{key}_{list_of_dicts.index(i)+1}.txt", "w") as result:
                json.dump({key: value}, result)