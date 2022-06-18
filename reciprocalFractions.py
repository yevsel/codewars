

class ReciprocalFractions:

    def largest_recurring_pattern(self):
        largest_pattern = []
        d = 0
        for i in range(1, 1000):
            if self.__recurring_pattern(str(1/i)):
                if len(self.__recurring_pattern(str(1/i))) > len(largest_pattern):          
                    largest_pattern = self.__recurring_pattern(str(1/i))
                    d = i
        return (largest_pattern, d)

    def __recurring_pattern(self, value):
        if len(value.split('.')[1]) > 8:
            decimal_portion = value.split('.')[1]
            first_eight = decimal_portion[0:8]
            starting_points = []
            for i in range(len(decimal_portion)-8):
                if decimal_portion[i]+decimal_portion[i+1]+decimal_portion[i+2] \
                   + decimal_portion[i+3] + decimal_portion[i+4] \
                        + decimal_portion[i+5] + decimal_portion[i+6] \
                   + decimal_portion[i+7] == first_eight:
                    starting_points.append(i)
            if len(starting_points) == 1:
                return False
            return decimal_portion[0:starting_points[1]]
        return False


r_cycles = ReciprocalFractions()

print("D with the longest occurence", r_cycles.largest_recurring_pattern())


>> "D with the longest occurence ('0.001017293997965412', 983)"

