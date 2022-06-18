from itertools import permutations


class Solution:
    def groupAnagrams(self, strs):
        valid_anagrams = []
        answers = []
        for word, possible_anagrams in self.__possible_anagrams(strs):
            arr = []
            for combination in possible_anagrams:
                if combination in strs:
                    arr.append(combination)
            answers.append(arr)
            arr = []
        lenghts = list(set([len(i) for i in answers]))
        for i in range(len(lenghts)):
            for j in range(len(answers)):
                if len(answers[j]) == lenghts[i]:
                    valid_anagrams.append(answers[j])
                    break
        return valid_anagrams

    def __possible_anagrams(self, strs):
        arr = []
        for i in range(len(strs)):
            arr.append((strs[i], [''.join(i)
                       for i in list(permutations(strs[i], len(strs[i])))]))
        return arr


a1 = Solution()
print(a1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
