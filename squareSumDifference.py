class SquareSumDifference:
    def sumOfSquares():
        ans = 0
        for i in range(1, 101):
            ans += i**2
        return ans

    def squareOfSums():
        ans = 0
        for i in range(1, 101):
            ans += i
        return ans**2


print(SquareSumDifference.squareOfSums()-SquareSumDifference.sumOfSquares())
