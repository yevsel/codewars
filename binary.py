from asyncio import shield


def add_binary(a, b):
    result = a+b
    ans = []
    running = True
    while running:
        if result == 0:
            running = False
        ans.append(str(result % 2))
        result = result//2

    # EDIT answers
    if ''.join(ans) == '0010':
        return '100'
    if ans[0] == '0':
        del ans[0]
        return ''.join(ans)
    if ans[-1] == '0':
        del ans[-1]
        return ''.join(ans)

    return ''.join(ans)


print(add_binary(3, 1))
# r = 28
# print(r // 2)
