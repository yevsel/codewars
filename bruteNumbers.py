from itertools import permutations
import numbers

nums = '0123456789'
perms = list(permutations(nums, 2))

# for i in range(len(perms)):
#     for j in range(len(perms)):
#         if int(''.join(perms[i]))+int(''.join(perms[j])) == 207:
#             print(perms[i], perms[i])
#             break

for i in perms:
    for j in perms:
        if int(''.join(i))+int(''.join(j)) == 207:
            print(i, j)
            break
        else:
            # print("No")
