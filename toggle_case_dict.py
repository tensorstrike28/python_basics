'''Write a function toggle_case_map(s) that:
Takes a lowercase string s
Returns a dictionary where:
Keys are characters from the string (no duplicates)
Values are the same character in uppercase if it occurs an even number of
    times, else in lowercase
'''

input_string = input().strip().lower()
freq_dict = {}
for character in input_string:
    freq_dict[character] = freq_dict.get(character, 0)+1
char_dict = {}
for key, value in freq_dict.items():
    if value % 2 == 0:
        char_dict[key] = key.upper()
    else:
        char_dict[key] = key
print(char_dict)
