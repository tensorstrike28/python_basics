list1 = input("Enter first list separated by space: ").split()
list2 = input("Enter second list separated by space: ").split()
out_list = []
for item1 in list1:
    if item1 not in out_list:
        if item1 in list2:
            out_list.append(item1)
print(f"Intersection: {out_list}")
