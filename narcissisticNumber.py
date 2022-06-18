
# A narcissistic number is a number that can be represented by some kind of mathematical manipulation of their digits
# Example (153 = 1**3 + 5**3 + 3**3) is called a perfect narcissistic number
# Return true if the argument is a narcissistic number

def narcissistic(value):

    num = []
    for i in range(len(str(value))):
        num.append(int(list(str(value))[i])**len(str(value)))
    if sum(num) == value:
        return True
    return False


print(narcissistic(371))

