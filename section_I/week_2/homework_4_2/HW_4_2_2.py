# Write a function that, based on the provided text, determines the percentage frequency of each unique character in that
#text.

# Example:
# Input: "say hello to my little friend"
# Output: {"a": 3.45, "d": 3.45, "e": 10.35, "f": 3.45, "h": 3.45, "i": 6.9, "l": 13.8, ..., " ": 17.24}

def find_character_count(text):
    unique_dict={}
    for c in text:
        if c in unique_dict:
            unique_dict[c] = unique_dict[c] + 1
        else:
            unique_dict[c] = 1
    return unique_dict

def find_character_frequency(dict1,total_count):
    for key in dict1:
        dict1[key] = round(dict1[key] * 100 / total_count,2)
    return dict1


    
input_string = "say hello to my little friend"
character_count_dict = find_character_count(input_string)
print(find_character_frequency(character_count_dict, len(input_string)))