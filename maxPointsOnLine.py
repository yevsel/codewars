"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
"""
from itertools import permutations
from math import ceil


class MaxPointsOnLine:
    def __init__(self, points):
        self.__points = points
        self.__perms = list(permutations(points, 2))
        self.__nonDuplicate = None

    def __commonPoints(self):
        slope = []
        max_occurence = []
        for points in self.__perms:
            try:
                slope.append(self.__gradient(points))
            except ZeroDivisionError:
                pass
        self.__nonDuplicate = list(set(slope))

        for i in range(len(self.__nonDuplicate)):
            max_occurence.append(
                (self.__nonDuplicate[i], slope.count(self.__nonDuplicate[i])))
        return max_occurence

    def maxPoints(self):
        largest = 0
        for point, occurence in self.__commonPoints():
            if occurence > largest:
                largest = occurence
        return int(largest/ceil(len(self.__points)/2))

    def __gradient(self, points):
        return (points[1][1]-points[0][1])/(points[1][0]-points[0][0])


m1 = MaxPointsOnLine([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
print(f"Maximum common points: {m1.maxPoints()}")
