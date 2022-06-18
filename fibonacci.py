# Get fibonacci sequence
def fibonacci(times):
    a, b, c = 0, 1, 1
    for i in range(times):
        print(c, " ", end='')
        c = a+b
        a = b
        b = c

fibonacci(10)



# Factorial of a number
def factorial(num):
    ans = 1
    if num > 0:
        for i in range(1, num+1):
            ans *= i
    return ans
print(factorial(5))


# Palindromic numbers within any range
palindrom = [i for i in range(10000, 100000) if str(i) == str(i)[::-1]][0:10]
print(palindrom)

