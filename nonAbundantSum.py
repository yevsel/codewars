

class NonAbundantSum:
    def __init__(self):
        self.all_abundant_nums = [i for i in range(
            1, 28124) if self.__is_abundant_number(i)]
        self.sums = []

    def sums_of_two(self):
        sum_of_two = 0
        for i in self.all_abundant_nums:
            print(i)
            for j in self.all_abundant_nums:
                sum_of_two = i+j
                if self.__is_abundant_number(sum_of_two)\
                        and sum_of_two in self.all_abundant_nums:
                    self.sums.append(sum_of_two)
                    sum_of_two = 0
                sum_of_two = 0
        # Finding all numbers that can be written as sum of two abundant numbers

        # Subtracting the two arrays, Using set and returning thier sum
        return sum(list(set(self.all_abundant_nums).difference(set(self.sums))))

    def __is_abundant_number(self, num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) > num


n1 = NonAbundantSum()
# print(non1.check_status(24))

print("Answer", n1.sums_of_two())


# >> "Answer 4179871"
