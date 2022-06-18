class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        self.__rec1_width = ax2-ax1
        self.__rec1_height = ay2-ay1
        self.__rec2_width = bx2-bx1
        self.__rec2_height = by2-by1
        area_1 = self.__rec1_height*self.__rec1_width
        area_2 = self.__rec2_height*self.__rec2_width
        return self.__total_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)-self.__empty_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)

    def __empty_area(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        width = bx2-ax2
        height = ay2 - by2
        width_2 = bx1-ax1
        height_2 = ay1-by1
        return (width*height) + (width_2*height_2)

    def __total_area(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        width = bx2-ax1
        height = ay2-by1
        return width*height


s1 = Solution()
# print(s1.computeArea(-2, -2, 2, 2, -2, -2, 2, 2))
print(s1.computeArea(0, 0, 0, 0, -1, -1, 1, 1))
