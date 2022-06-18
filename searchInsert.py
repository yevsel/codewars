def searchInsert(nums, target):
    numbers = "0123456789"
    loc = None
    interval = []
    for i in range(len(nums)):
        if str(nums[i]) == str(target):
            loc = i
    if loc != None:
        return loc
    else:
        #Find interval that is greater than one
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 2:
                interval.append([nums[i], nums[i+1]])
                break
    return interval


print(searchInsert([1, 3, 5, 6], 2))
