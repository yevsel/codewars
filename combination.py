
# Return the mathematical combination of two numbers
# Example  12C5  =  792

def combination(n, x):

    def factorial(num):
        ans = 1
        for i in range(num):
            ans *= (num-i)
        return ans

    numerator = factorial(n)
    denominator = factorial(x)*factorial(n-x)

    return numerator//denominator


print(combination(12, 5))
