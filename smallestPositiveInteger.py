
class SmallestPositiveInteger:
    def __init__(self, number):
        self.__number = number

    def __move(self):
        string = list(str(self.__number))
        first_value = string[0]
        del string[0]
        string.append(first_value)
        return int(''.join(string))

    def check_condition(self):
        value = self.__move()
        if round(value/self.__number, 1) == 3.2:     
            return True
        return False


s1 = SmallestPositiveInteger(2958)
print(s1.check_condition())
