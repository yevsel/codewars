# Write a program that finds all integer solutions to Pell’s equation x^2 − 2y^2 = 1, where x and y are between 1 and 100


def pells_equation():
    ans = []
    def f(x, y): return x**2 - 2*(y**2)

    for i in range(1, 101):
        for j in range(1, 101):
            if f(i, j) == 1:
                ans.append([i, j])
    return ans


print(pells_equation())
