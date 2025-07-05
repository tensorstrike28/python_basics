def tuple_from_list(list1, list2):
    out_list = []
    for i in range(min(len(list1), len(list2))):
        out_list.append(tuple((list1[i], list2[i])))
    return (out_list)


input_list1 = input("Enter first list separated by space: ").split()
input_list2 = input("Enter second list separated by space: ").split()
print(
    f"Output list: {tuple_from_list(input_list1,input_list2)}")
