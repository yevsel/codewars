from itertools import permutations
from numpy import cbrt


class Cubic_Permutations:
    def __init__(self, cube_value):
        self.__value = cube_value

    def __repr__(self) -> str:
        return """
            The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

            Find the smallest cube for which exactly five permutations of its digits are cube.
        """

    def __get_cube_roots(self, number):
        ans = []
        for perm in permutations(str(number), len(str(number))):
            if str(cbrt(int(''.join(perm)))) == str(round(cbrt(int(''.join(perm))), 1)):
                ans.append(perm)

        return list(set([(int(''.join(i))) for i in ans]))

    def perfect_cube(self):
        for num in range(1, 5000):
            if len(self.__get_cube_roots(num**3)) > 2:
                print(self.__get_cube_roots(num**3), num**3, '==>', num)


s1 = Cubic_Permutations(1234)
print(s1.perfect_cube())
