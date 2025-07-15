'''
Write a function group_by_length(words) that:
Takes a list of strings words
Returns a dictionary where:
Keys are word lengths (integers)
Values are lists of words having that length
The order of words in the lists must match the original input order
'''


def group_by_length(input_list):
    len_dict = {}
    for word in input_list:
        length = len(word)
        if length in len_dict:
            len_dict[length].append(word)
        else:
            len_dict[length] = [word]
    return(len_dict)


input_list = input().split()
print(group_by_length(input_list))
