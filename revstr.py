def revstr(input_string):
    reversed_string = []
    for x in range(len(input_string)-1, -1, -1):
        reversed_string.append(input_string[x])
    return (''.join(reversed_string))


input_str = input("Enter string: ")
print(f"Reversed string is {revstr(input_str)}")
