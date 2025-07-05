input_list = input("Enter inputs separated by space: ").split()
length = len(input_list)
for i in range(length//2):
    temp = input_list[i]
    input_list[i] = input_list[length-1-i]
    input_list[length-1-i] = temp
print(f"reversed_list: {input_list}")
