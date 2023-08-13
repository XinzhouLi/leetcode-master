#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        for p0 in range(len(nums)):
            if nums[p0] == val:
                continue
            nums[p1] = nums[p0]
            p1 += 1
            print(nums)
        return p1 

# @lc code=end

