input_str_1 = "Hello World"
input_str_2 = "Python is Awesome"

def reverse_words_and_swap_case(input_str):
    words = input_str.split()
    new_words = []
    for word in words:
        reversed_word = word[::-1]
        swapped_word = reversed_word.swapcase()
        new_words.append(swapped_word)
    return " ".join(new_words)

print(reverse_words_and_swap_case(input_str_1))
print(reverse_words_and_swap_case(input_str_2))