def clean(string_in):
    string_list = string_in.strip().lower().split()
    filtered_string_list = []
    for word in string_list:
        filtered_word = "".join(
            character for character in word if ord(character) in range(97, 123))
        filtered_string_list.append(filtered_word)
    return (filtered_string_list)


file = open("sample.txt")
string_list = clean(file.read())
file.close()
freq_dict = {}
for word in string_list:
    freq_dict[word] = freq_dict.get(word, 0)+1
print(freq_dict)
