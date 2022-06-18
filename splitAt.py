

class RemoveCharacterAt:
    def __init__(self, text, character):
        self.__chr = character
        self.__text = text

    def split(self):
        hold = ''
        splitted = []
        for i in range(len(self.__text)):
            if self.__text[i] == self.__chr:
                splitted.append(hold)
                hold = ''
            else:
                hold += self.__text[i]
        splitted.append(hold)
        return ' '.join(splitted)
