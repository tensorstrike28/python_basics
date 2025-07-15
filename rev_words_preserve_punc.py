'''
Write a function reverse_words_preserve_punctuation(s) that:
Takes a sentence s
Reverses each word individually (not the order of words)
Keeps punctuation marks locked at the end of words
Handles ., ,, !, ? only as punctuation
Maintains spacing and word order exactly as input
'''


def reverse_words_preserve_punctuation(in_string):
    i = 0
    rev_str = ""
    while (i < len(in_string)):
        start_char = i
        while (True):
            if (in_string[i] in [".", ",", "!", "?", " "]):
                rev_str += (in_string[i-1:start_char-1:-1] + in_string[i])
                i += 1
                break
            elif (i < len(in_string)-1):
                i += 1
            else:
                rev_str += (in_string[i:start_char-1:-1])
                i += 1
                break
    print(rev_str.strip())


input_string = input()
reverse_words_preserve_punctuation(" " + input_string)
