def unique_chars(s):
    dict_freq = {}
    uniq_char = []
    for i in s:
        dict_freq[i] = dict_freq.get(i, 0) + 1
    for key, value in dict_freq.items():
        if value == 1:
            uniq_char.append(key)
    return (uniq_char)


input_string = input().strip()
print(unique_chars(input_string))
