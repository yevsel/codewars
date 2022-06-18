from itertools import permutations


def generator():
    yield permutations("ABCD", 3)


for i in generator():
    print(i)
