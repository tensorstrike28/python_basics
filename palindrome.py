def is_palindrome(input_string):
    reference_string = sanitise_string(input_string)
    reversed_string = []
    for x in range(len(reference_string)-1, -1, -1):
        reversed_string.append(reference_string[x])
    return (''.join(reversed_string) == reference_string)


def sanitise_string(input_string):
    sanitised_string = []
    for character in input_string:
        if 97 <= ord(character) <= 122:
            sanitised_string.append(character)
    return (''.join(sanitised_string))


input_string = input("Enter string: ").lower()
message = "The entered string is a palindrome" if(is_palindrome(
    input_string)) else "The entered string is not a palindrome"
