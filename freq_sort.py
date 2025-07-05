def freq_sort(input_list):
    freq_dict = {}
    for item in input_list:
        freq_dict[item] = freq_dict.get(item, 0)+1
    item_list = list(freq_dict.keys())
    freq_list = list(freq_dict.values())
    for i in range(len(freq_list)):
        for j in range(i, len(freq_list)):
            if freq_list[j] > freq_list[i]:
                temp_freq = freq_list[i]
                freq_list[i] = freq_list[j]
                freq_list[j] = temp_freq
                temp_item = item_list[i]
                item_list[i] = item_list[j]
                item_list[j] = temp_item
    sorted_list = []
    for i in range(len(freq_list)):
        sorted_list.extend(item_list[i] * int(freq_list[i]))
    return (sorted_list)


input_list = input("Enter items with space: ").split()
print(f"Freq sort: {freq_sort(input_list)}")
