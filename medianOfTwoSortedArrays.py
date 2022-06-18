

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        self.__concat = nums1+nums2
        self.__sort()
        self.__half = int(len(self.__concat)/2)
        if len(self.__concat) % 2 != 0:
            return float(self.__concat[self.__half])
        return (self.__concat[self.__half]+self.__concat[self.__half-1])/2

    def __sort(self):
        for i in range(len(self.__concat)-1):
            for j in range(len(self.__concat)-1):
                if self.__concat[j+1] < self.__concat[j]:
                    self.__concat[j+1], self.__concat[j] = self.__concat[j], self.__concat[j+1]


s1 = Solution()
print(s1.findMedianSortedArrays([14, 6, 4, 4], [5, 2]))
