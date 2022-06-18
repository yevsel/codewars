

class AmicableNumbers:
    def __init__(self):
        self.__amicable_pairs = []

    def __d(self, num):
        ans = 0
        for i in range(1, num):
            if num % i == 0:
                ans += i
        return ans

    def sum_of_amicable_pairs(self):
        first_sum = 0
        for i in range(1, 10001):
            first_sum = self.__d(i)
            if self.__d(first_sum) == i and first_sum != i:
                self.__amicable_pairs.append((first_sum, i))
                first_sum = 0
            first_sum = 0

        # Remove duplicates
        arr = [sorted(i) for i in self.__amicable_pairs]
        arr2 = []
        for i in range(len(arr)):
            if arr[i] not in arr2:
                arr2.append(arr[i])
        return arr2


amicable = AmicableNumbers()

sum_of_pairs = 0
for k, v in amicable.sum_of_amicable_pairs():
    sum_of_pairs += (k+v)

print("Sum of amicable pairs are", sum_of_pairs)
