input_strings = list(input("Enter list separated by space: ").split())
dict_list = {}
anagram_list = []
for word in input_strings:
    sorted_word = ''.join(sorted(word))
    if sorted_word in dict_list:
        dict_list[sorted_word].append(word)
    else:
        dict_list[sorted_word] = [word]
for key in dict_list:
    anagram_list.append(dict_list[key])
print(f"Anagram list: {anagram_list}")
