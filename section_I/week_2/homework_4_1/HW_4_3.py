# Write a function that finds unique values in a given list of tuples and prints them to the standard output.

# [("h", "g", "l", "k"), ("a", "b", "d", "e", "c"), ("j", "i", "y"), ("n", "b", "v", "c"), ("x", "z")]

t = [("h", "g", "l", "k"), ("a", "b", "d", "e", "c"),
     ("j", "i", "y"), ("n", "b", "v", "c"), ("x", "z")]


def find_character_count(tuple_list):
    unique_dict = {}
    for t in tuple_list:
        for c in t:
            if c not in unique_dict:
                unique_dict[c] = 1
            else:
                unique_dict[c] = unique_dict[c] + 1
    return unique_dict


def find_unique_characters(input_dict):
    unique_list = []
    for key in input_dict:
        if input_dict[key] == 1:
            unique_list.append(key)
    return unique_list


char_count_dict = find_character_count(t)
print(find_unique_characters(char_count_dict))
