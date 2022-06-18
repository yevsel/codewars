

class DigitFifthPowers:

    def __init__(self):
        self.__sums = []

    def __repr__(self):
        return """
        This class computes the sum of each number raised            
        to the power of another number.
        """

    def compute_answer(self, power):
        for i in range(1_000, 500_000):
            if self.__sum_of_powers(i, power):
                # print(i)
                self.__sums.append(i)
        return sum(self.__sums)

    def __sum_of_powers(self, num, power):
        # Split the numbers into corresponding digit
        digits = [int(i) for i in str(num)]
        return num == sum([i**power for i in digits])


DFP = DigitFifthPowers()
print("Sum is", DFP.compute_answer(5))


# >> "Sum is 443839"
