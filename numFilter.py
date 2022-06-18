# Return an array of only numbers contained in a list

def filter_list(theList: list):
    only_strings = [str(i) for i in theList]
    nums = []

    for i in range(len(theList)):
        if only_strings[i] != theList[i]:
            nums.append(theList[i])
    return nums


print(filter_list([86, 3, '1', '123', 123, 's']))
