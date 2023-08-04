#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        else:
            stack = []
            for i in s:
                if i == '(' or i == '[' or i == '{':
                    stack.append(i)
                elif (len(stack) > 0) and ((i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{')):
                    stack.pop()
                else:
                    return False
            if len(stack) == 0:
                return True

# @lc code=end

