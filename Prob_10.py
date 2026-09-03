input_string_1 = "Hello World"
input_string_2 = "Wonderful World"

def sort_characters_in_each_word_alphabetically(input_string):
    input_string = input_string.lower()
    
    words = input_string.split(" ")

    new_words = []

    for word in words:
        sorted_word = "".join(sorted(word))
        new_words.append(sorted_word)

    return " ".join(new_words)

print(sort_characters_in_each_word_alphabetically(input_string_1))
print(sort_characters_in_each_word_alphabetically(input_string_2))