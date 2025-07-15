'''
Write a function letter_indices(word) that:
Takes a single lowercase string word
Returns a dictionary where:
Keys are characters (a–z)
Values are lists of indices where that character appears in the string
'''


def letter_indices(str_input):
    index_dict = {}
    for i in range(len(str_input)):
        if str_input[i] in index_dict:
            index_dict[str_input[i]].append(i)
        else:
            index_dict[str_input[i]] = [i]
    return index_dict


input_string = input().strip().lower()
print(letter_indices(input_string))
