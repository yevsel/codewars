from itertools import permutations


class FourSums:
    def fourSum(self, nums, target):
        answers = []
        perms = list(permutations(nums, 4))

        for i in range(len(perms)):
            if sum(perms[i]) == target:
                a = list(perms[i])
                answers.append(a)
        arr_2 = []
        for i in range(len(answers)):
            if self.__check_existence(arr_2, self.__sort_arr(answers[i])):
                arr_2.append(answers[i])
        return arr_2

    def __sort_arr(self, arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[j+1] < arr[j]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
        return arr

    def __check_existence(self, arr, value):
        for i in range(len(arr)):
            if self.__sort_arr(arr[i]) == value:
                return False
        return True


solution = FourSums()
print(solution.fourSum([1, 0, -1, 0, -2, 2], target=0))

# >> [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]

print(solution.fourSum([2, 2, 2, 2, 2], target=8))
# >>[[2, 2, 2, 2]]
