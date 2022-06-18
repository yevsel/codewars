from time import process_time
from string import ascii_letters
from itertools import permutations
from math import perm
from random import choice


class BruteForceAttack:
    def __init__(self, possible_combinations=3):
        self.__alphanumeric = ascii_letters+"1234567890"
        self.__possible_combinations = possible_combinations
        self.__combinations = list(permutations(
            self.__alphanumeric, possible_combinations))

    def average_time_taken(self):
        execution_times = []
        for i in range(20):
            random_password = choice(self.__combinations)
            start_time = process_time()
            for j in range(perm(len(self.__alphanumeric), self.__possible_combinations)):
                if random_password == self.__combinations[j]:
                    execution_times.append(process_time()-start_time)
                    break
        average_time = sum(execution_times)/len(execution_times)
        return average_time


brute1 = BruteForceAttack(4)
print("Average time taken:", brute1.average_time_taken(), "seconds")
