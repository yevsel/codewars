
# How to reverse a string

def reverse(text):
    rev = ""
    for i in range(len(text)):
        rev += text[(len(text)-1)-i]
    return rev


print(reverse("Selasi"))
