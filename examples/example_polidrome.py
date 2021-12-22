def palidrome (word):
    word = word.lower()
    return word[::-1] == word
print(palidrome("МАМА"))
print(palidrome("МАМ"))