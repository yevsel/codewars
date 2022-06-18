from itertools import permutations


class PrimePermutations:
    def __init__(self):
        # Get all prime numbers
        self.__all_primes = [i for i in range(
            1000, 9999) if self.__is_prime(i)]
        self.__answers = []

    def compute_answer(self):
        for i in self.__all_primes:
            # Store permutations of each number if its a prime
            primes_of_permutation = [int(''.join(i)) for i in list(
                permutations(str(i), 4)) if self.__is_prime(int(''.join(i)))]         
            # Check if its arithmetic sequence
            for j in permutations(primes_of_permutation, 3):
                if self.__arithmetic_seq(j):
                    self.__answers.append(j)
                    break
        return self.__answers

    def __is_prime(self, num):
        arr = [i for i in range(2, num+1) if num % i == 0]
        if len(arr) == 1 and arr[0] == num:
            return True
        return False

    def __arithmetic_seq(self, arr):
        # Check if a sequence is an arithmetic sequence
        difference = arr[1]-arr[0]
        if difference == 0:
            return False
        if arr[0] > arr[1]:
            return False
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] != difference:
                return False
        return True


solution = PrimePermutations()
print(solution.compute_answer())


>> "(1487, 4817, 8147) (2969, 6299, 9629)"

