input_list = list(map(int,
                      input("Enter numbers separated by space: ").split()))
maxnum = input_list[0]
for num in input_list[1:]:
    if num > maxnum:
        maxnum = num
print(f"Maximum number is {maxnum}")
