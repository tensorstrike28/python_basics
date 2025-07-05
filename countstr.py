input_string = input("Enter the string: ").strip()
dict = {}
for x in input_string:
    dict[x] = dict.get(x, 0) + 1
for key, value in dict.items():
    print(f"\n{key} occurred {value} times")
