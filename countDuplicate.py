def duplicate_count(text):
    # Check if they ae numbers
    nums = '0123456789'
    they_are_nums = 0
    for i in range(len(text)):
        if text[i] in nums:
            they_are_nums += 1
    if they_are_nums == len(text):
        return len(text)
    nonDuplicates = []
    count = []
    the_return = []
    new_text = str(text).lower().strip()
    for i in range(len(text)):
        if new_text[i] not in nonDuplicates:
            nonDuplicates.append(new_text[i])
    # Counting them
    for i in range(len(nonDuplicates)):
        amount = 0
        for j in range(len(new_text)):
            if nonDuplicates[i] == new_text[j]:
                amount += 1
        count.append((nonDuplicates[i], amount))

    # How to return
    for (k, v) in count:
        if v > 1:
            the_return.append(str(v))
    # the_string = ''.join(str(the_return))
    if the_return:
        # print(count)
        return len(the_return)
    else:
        # print(count)
        return 0


print(duplicate_count("indivisibility"))


# duplicate_count("selasi Yevoo is yh my name")
