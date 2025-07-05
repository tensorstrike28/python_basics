def check_anagram(str1, str2):
    return(sorted(str1) == sorted(str2))


def anagrams(input_list):
    anagram_list = []
    mask_list = [False]*len(input_list)
    for i in range(len(input_list)):
        if not mask_list[i]:
            check_list = []
            for j in range(i, len(input_list)):
                if check_anagram(input_list[i], input_list[j]):
                    check_list.append(input_list[j])
                    mask_list[j] = True
            anagram_list.append(check_list)
    return anagram_list


input_strings = list(input("Enter list separated by space: ").split())
print(f"Anagram list: {anagrams(input_strings)}")
