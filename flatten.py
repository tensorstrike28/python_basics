import ast


def flat_lst(input_list):
    simple_list = []
    for item in input_list:
        if type(item) is not list:
            simple_list.append(item)
        else:
            simple_list.extend(flat_lst(item))
    return (simple_list)


input_list = ast.literal_eval(input("Enter a nested list: "))
print(type(input_list))
print(f"Flattened list: {flat_lst(input_list)}")
