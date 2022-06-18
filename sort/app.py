numbers = [8, 3, 4, 2, 5, 1, 5, 7]
for j in range(len(numbers)-1):
    for i in range(len(numbers)-1):
        if (numbers[i+1] < numbers[i]):
            numbers[i+1], numbers[i] = numbers[i], numbers[i+1]
# print(numbers)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


persons = [Person("Selasi", 23), Person("Princess", 12),
           Person("Yevoo", 31), Person("Justice", 1)]

people = []
# for i in range(len(persons)-1):
#     for j in range(len(person))

l = [
    [1, 4, 6],
    [6, 3, 1],
    [8, 2, 4]
]

count = 0
for i in range(3):
    for j in range(3):
        if l[i][j] % 2 == 0:
            count += 1
# print(count)

print([2]*5)
