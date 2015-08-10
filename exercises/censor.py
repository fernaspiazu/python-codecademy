__author__ = 'fumandito'


def censor(text, word):
    new_phrase = []
    for p in text.split():
        if p == word:
            new_phrase.append("*" * len(word))
        else:
            new_phrase.append(p)

    return " ".join(new_phrase)


print censor("hello world hello marica", "hello")
