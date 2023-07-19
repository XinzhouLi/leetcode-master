#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0 
        end = 0
        longest = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s))[::-1]:
            for j in range(len(s)):            
                if i>j:
                    continue
                if s[i] ==  s[j]:
                    if i == j or i+1 == j:
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        dp[i][j] =True
                if j-i+1 >= longest and dp[i][j]:
                    longest = j-i+1
                    start, end = i, j
        return s[start:end+1]
# @lc code=end

