#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        if nums[0] > 0:
            return []
        result = set()
        p1 = 0
        p3 = len(nums)-1
        for p1 in range(p3-1):
            if p1 > 0 and nums[p1] == nums[p1-1]: 
                continue
            p2 = p1+1
            p3 = len(nums)-1
            while p2<p3:
                sum = nums[p1] + nums[p2] + nums[p3]
                if sum < 0:
                    p2 += 1
                elif sum > 0:
                    p3 -= 1
                elif sum == 0 :
                    result.add((nums[p1], nums[p2], nums[p3]))   
                    p2 += 1
                    p3 -= 1
        result = list(result)
        return result
# @lc code=end

