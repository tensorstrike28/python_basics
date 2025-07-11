'''Write a function filtered_squares(lst) that:
Takes a list of integers lst
Returns a list of squares of only the positive odd numbers
Do it in a single list comprehension
Preserve order
'''
input_list = list(map(int, input().split()))
output_list = [i**2 for i in input_list if (i > 0 and i % 2 != 0)]
print(output_list)
