

class ConsecutivePrimes:

    def prime_numbers(self, num):
        is_prime = True
        ans = []
        for i in range(2, num):
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                ans.append(i)
            is_prime = True
        return ans

    def longest_sum(self):
        # Just be adding once there a break stop and append and continue
        long_runs = []
        arr = self.prime_numbers(1000)
        ans = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                ans += arr[j]
                if ans in arr:
                    long_runs.append([j, ans])
                    ans = 0
        # Largest
        return long_runs


a = ConsecutivePrimes()
print(a.longest_sum())
# print(a.prime_numbers(1000))
