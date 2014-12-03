def rot13(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o,' 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    for position, letter in enumerate(text):
        if(letter.isalpha()):
            text[position] = alphabet[(alphabet.index(letter.lower()) + 13)]
    return text


print rot13("test")
