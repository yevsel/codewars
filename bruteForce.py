
import time
from itertools import permutations
from string import ascii_letters
from random import choice


def get_time(seconds):
    hour = seconds//3600
    remainder = seconds % 3600
    minute = remainder//60
    sec = remainder % 60
    return f"{hour}hr :{minute}min :{sec}sec"

# Lets pick an arbitrarry number in the possible combinations


combinations = list(permutations(ascii_letters, 3))
random = ''.join(choice(combinations))
# print(''.join(choice(combinations)))

times = []

# Start
start = time.process_time()
for i in range(len(combinations)):
    if ''.join(combinations[i]) == random:
        times.append([time.process_time()-start, ''.join(combinations[i])])
        print(''.join(combinations[i]))
        break
end = time.process_time()


print(end-start)
print(random)
print(times)
