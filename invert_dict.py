n = int(input("Enter number of pairs: ").strip())
print("Enter key value pairs separated by space in each line:\n")
in_dict = {}
for _ in range(n):
    key, value = input().strip().split()
    in_dict[key] = value
rev_dict = {}
for key, value in in_dict.items():
    if value not in rev_dict:
        rev_dict[value] = [key]
    else:
        rev_dict[value].append(key)
print(rev_dict)
