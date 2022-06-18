import re


class Solution:
    def isMatch(self, s, p):
        self.text = s
        self.pattern = p
        ans = re.match(self.pattern, self.text)
        if ans:
            print(ans)
            return True
        print(ans)
        return False


s1 = Solution()
print(s1.isMatch('selasi', ""))
