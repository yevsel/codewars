
nums = "1234567890"
alpha = "CD"
symbol = "+"


ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
record = []

# twitter = @yevsel
# IG = @yev.sel

for i in range(len(ops)):
    if ops[i] in alpha:
        if ops[i] == "C":
            record.pop(-1)

        elif ops[i] == "D":
            ans = record[len(record)-1]*2
            record.append(ans)

    elif ops[i] in symbol:
        if ops[i] == "+":
            ans = record[len(record)-1]+record[len(record)-2]
            record.append(ans)

    elif str(abs(int(ops[i]))) in nums:
        record.append(int(ops[i]))


print(sum(record))
