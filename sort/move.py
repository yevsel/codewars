num = [3, 5, 1, 6]
for i in range(len(num)-1):
    num[i], num[i+1] = num[i+1], num[i]
