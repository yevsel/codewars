class PentagonNumbers:

    def __init__(self):
        pass

    # Function
    def __f(self, x): return x*((3*x)-1)/2

    # Pentagon numbers in an array
    def arr(self):
        arr = []
        for i in range(1, 1001):
            arr.append(int(self.__f(i)))

        # Check for conditions
        pentagonal_pairs = []

        for i in arr:
            for j in arr:
                if i+j in arr:
                    if j > i and j-i in arr:
                        pentagonal_pairs.append((i, j))
        return pentagonal_pairs


p = PentagonNumbers()
print(p.arr())
