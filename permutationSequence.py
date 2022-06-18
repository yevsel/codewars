from itertools import permutations

# Return the kth sequence of all possible combination of n numbers


class Solution:
    def getPermutation(self, n, k):
        alpha = []
        for i in range(1, n+1):
            alpha.append(str(i))
        perms = [i for i in list(permutations(alpha))]
        return ''.join(perms[k-1])


solution_one = Solution()
print(solution_one.getPermutation(4, 9))

# (1,2,3) => (123,132,231,213,312,321)
