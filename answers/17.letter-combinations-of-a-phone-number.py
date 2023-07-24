#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def wfs(self, digits, map, previous, current):
        result = []
        if current == len(digits):
            return [previous]
        else:
            for char in map[int(digits[current])]:

                result.extend(self.wfs(digits, map, previous+char, current+1))
            return result
    def letterCombinations(self, digits: str) -> List[str]:
        init = ord('a')
        map = {}
        for i in range(2,10):
            if i == 7 or i == 9:
                map[i] = [chr(j) for j in range(init, init+4)]
                init += 4
                continue
            map[i] = [chr(j) for j in range(init, init+3)]
            init += 3
        if digits == "":
            return []
        return self.wfs(digits, map, "", 0)

# @lc code=end

