def power_digit_sum(num):
    ans = list(str(2**num))
    ans2 = 0
    for i in range(len(ans)):
        ans2 += int(ans[i])
    return ans2


print(power_digit_sum(1000))
