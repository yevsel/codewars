from math import sqrt

# Return the next square if function argument is a square, -1 otherwise  

def find_next_square(number):
    num = sqrt(number)
    if num-int(num) != 0:
        return -1
    else:
        next = num+1
        return int(next*next)

    # return -1
print(find_next_square(144))
# >> 169
# print(find_next_square(12))
# >> -1
