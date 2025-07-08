"""
Write a function char_frequency(s) that:
Takes a lowercase string s
Returns a list of tuples (char, freq)
Sorted by: Highest frequency first
If equal frequency, then alphabetically
"""


def freq_tuple(in_string):
    freq_list = []
    unq_str = []
    for c in in_string:
        if c not in unq_str:
            unq_str.append(c)
    for x in unq_str:
        freq = 0
        for y in in_string:
            if x == y:
                freq += 1
        freq_list.append(tuple((x, freq)))
    return(list_sort(freq_list))


def list_sort(in_list):
    sort_pos = 1
    while (sort_pos < len(in_list)):
        for i in range(sort_pos):
            if (in_list[sort_pos][1] > in_list[i][1]):
                in_list.insert(i, in_list.pop(sort_pos))
            elif (in_list[i+1][1] < in_list[sort_pos][1] < in_list[i][1]):
                in_list.insert(i+1, in_list.pop(sort_pos))
            elif in_list[sort_pos][1] == in_list[i][1]:
                if (in_list[sort_pos][0] < in_list[i][0]):
                    in_list.insert(i, in_list.pop(sort_pos))
                elif (in_list[i+1][0] > in_list[sort_pos][0] > in_list[i][1]):
                    in_list.insert(i+1, in_list.pop(sort_pos))
        sort_pos += 1
    return(in_list)


input_string = input("Enter the string: ").strip().lower()
print(freq_tuple(input_string))
