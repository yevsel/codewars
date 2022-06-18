# An isogram string is a string where the occurence of each letter is exactly once.

def is_isogram(text):
    word = list(text.lower())
    nonDuplicate = list(set(word))
    if len(nonDuplicate) == len(word):
        return True
    else:
        return False


print(is_isogram("aba"))


