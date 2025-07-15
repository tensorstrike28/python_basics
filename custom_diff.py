'''
Write a function custom_diff(list1, list2) that:
Takes two lists of strings
Returns a list of strings in list1 but not in list2
Preserve order from list1
Don’t use set(), dict(), or any libraries
Don’t use in inside list comprehension
'''


def custom_diff(list1, list2):
    diff_list = []
    for item1 in list1:
        is_present = False
        for item2 in list2:
            if item1 == item2:
                is_present = True
                break
        if (not is_present):
            diff_list.append(item1)
    return diff_list


list1 = input().split()
list2 = input().split()
print(custom_diff(list1, list2))
