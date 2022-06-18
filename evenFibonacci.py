

class EvenFibonacci:

    def sum_of_even(self):
        a, b = 0, 1
        even = []
        while True:
            c = a+b
            if c >= 4_000_000:
                break
            elif c % 2 == 0:
                even.append(c)
            a = b
            b = c
        return even


e = EvenFibonacci()
print(sum(e.sum_of_even()))
