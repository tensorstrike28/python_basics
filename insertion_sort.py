def insertion_sort(in_list):
    sort_pos = 1
    while (sort_pos < len(in_list)):
        for i in range(sort_pos):
            if (in_list[sort_pos] > in_list[i]):
                in_list.insert(i, in_list.pop(sort_pos))
            elif (in_list[i+1] < in_list[sort_pos] < in_list[i]):
                in_list.insert(i+1, in_list.pop(sort_pos))
        sort_pos += 1
    return(in_list)


input_list = list(
    map(int, input("Enter numbers seperated by space: ").strip().split()))
print(insertion_sort(input_list))
