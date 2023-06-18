def roman_to_int(roman: str) -> int:
    roman_dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }

    roman = roman.strip()

    result = 0

    i = 0
    while i < len(roman):
        if i+1 < len(roman) and roman[i:i+2] in roman_dict:
            result += roman_dict[roman[i:i+2]]
            i += 2
        else:
            result += roman_dict[roman[i]]
            i += 1

    return result