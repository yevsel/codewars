

class Solution:
    def threeSum(self, nums):
        unique_triplets = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        if i != j and i != k and j != k:
                            unique_triplets.append([nums[i], nums[j], nums[k]])      

        # Sorting all the list in the unique triplets
        arr = []
        for i in range(len(unique_triplets)):
            if self.__not_member(self.__sort(unique_triplets[i]), arr):
                arr.append(unique_triplets[i])
        return arr

    def __sort(self, arr):
        # Sorting in ascending order
        array = arr
        for i in range(len(array)-1):
            for j in range(len(array)-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    def __not_member(self, member, group):
        # Checking for duplicates
        for i in range(len(group)):
            if group[i] == member:
                return False
        return True


s1 = Solution()
print(s1.threeSum([-1, 0, 1, 2, -1, -4]))



# >> [[-1, 0, 1], [-1, -1, 2]]
