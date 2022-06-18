# Return True if the list argument is an increasing sequence

def isIncreasing(inlist):

    increasing = True
    for i in range(len(inlist)-1):
        if inlist[i+1] <= inlist[i]:
            increasing = False
            break
    return increasing


print(isIncreasing([1, 2, 3, 1, 4]))


# >> False
