from string import ascii_letters


class CamelCase:

    def toCamel(text):
        split_at = ""
        change = False
        for letter in text:
            if letter not in ascii_letters:
                change = True
                split_at = letter
                break
        if change:
            arr = text.split(split_at)
            # Check
            the_first = ""
            if arr[0][0] == arr[0][0].lower():
                the_first = arr[0]
                del arr[0]
                return the_first+''.join([i.capitalize() for i in arr])   
            return ''.join([i.capitalize() for i in arr])
        else:
            # Return the text if its already in camelCase
            return text


print(CamelCase.toCamel("theStealthWarrior"))
# theStealthWarrior
print(CamelCase.toCamel("The_Stealth_Warrior"))
# TheStealthWarrior
print(CamelCase.toCamel("saviour^Jesus^christ"))
# saviourJesusChrist





def to_camel_case(text):
    split_at = ""
    change = False
    for i in text:
        if i not in ascii_letters:
            change = True
            split_at = i
            break
    if change:
        arr = text.split(split_at)
        # Check
        the_first = ""
        if arr[0][0] == arr[0][0].lower():
            the_first = arr[0]
            del arr[0]
            return the_first+''.join([i.capitalize() for i in arr])
        return ''.join([i.capitalize() for i in arr])
    else:
        return text


# print(to_camel_case("TheStealthWarrior"))
# print(ascii_letters)
