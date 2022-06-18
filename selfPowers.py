def self_powers():
    ans = 0
    for i in range(1, 1001):
        ans += i**i
    return ans


print(self_powers())
