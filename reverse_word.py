def reverse_word(x):
    return (x[::-1])


input_words = input("Enter string Aegis bhai: ").strip().split(' ')
reversed_words = []
for word in input_words:
    reversed_words.append(reverse_word(word))
print(' '.join(reversed_words))
