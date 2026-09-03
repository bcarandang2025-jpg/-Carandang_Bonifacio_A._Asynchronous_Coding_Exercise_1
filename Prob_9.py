input_word_1 = "Hello"
input_word_2 = "Corporation"
input_word_3 = "Python"

def count_and_list_repeated_characters(input_word):
    char_count = {}
    for char in input_word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    repeated_chars = []

    for char, count in char_count.items():
        if count > 1:
            repeated_chars.append(char)

    repeated_chars.sort()

    print(len(repeated_chars))

    if len(repeated_chars) > 0:
        print(" ".join(repeated_chars))
    else:
        print("None")

count_and_list_repeated_characters(input_word_1)
count_and_list_repeated_characters(input_word_2)
count_and_list_repeated_characters(input_word_3)