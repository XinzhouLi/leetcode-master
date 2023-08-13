#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        next = self.commonLength(needle)
        p1 = 0
        p2 = 0
        while p1 < len(haystack) :
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            elif haystack[p1] != needle[p2]:
                if p2-1 < 0:
                    p2 = 0
                else:
                    p2 = next[p2-1]
                while haystack[p1] != needle[p2] and p2 > 0:
                    if p2-1 < 0:
                        p2 = 0
                    else:
                        p2 = next[p2-1]
                if haystack[p1] ==  needle[p2]:
                    p1 += 1
                    p2 += 1
                    # continue
                else:
                    p1+=1
                    # continue
            if p2==len(needle):  
                return p1-p2
        return -1

    def commonLength(self, string) -> int:
        next = []
        p1 = 0
        for p2 in range(len(string)):
            if p2 == 0:
                next.append(0)
            elif string[p1] == string[p2]:
                p1 += 1
                next.append(next[p2-1]+1)
            elif string[p1] != string[p2]:
                
                p3 = p1-1
                p4 = next[p3]
                while string[p2] != string[p4] and p3 > 0:
                    p3 = p4-1
                    p4 = next[p3]
                if string[p2] == string[p4]:
                    next.append(next[p3]+1)
                else: 
                    next.append(0)
        return next



# @lc code=end

