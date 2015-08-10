__author__ = 'fumandito'


def anti_vowel(text):
    final_text = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in text:
        if letter.lower() not in vowels:
            final_text += letter

    return final_text


print anti_vowel("Hey you!")
