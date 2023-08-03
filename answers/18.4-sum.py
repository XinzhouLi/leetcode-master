#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        valueResult = []
        p4 = len(nums)-1
        for p1 in range(p4-2):
            if p1 != 0 and nums[p1] == nums[p1-1]:
                continue
            for p2 in range(p1+1,p4-1):
                p3 = p2+1
                p4 = len(nums)-1
                while p3<p4:
                    sum = nums[p1] + nums[p2] + nums[p3] + nums[p4]
                    valueAns = [nums[p1], nums[p2], nums[p3], nums[p4]]
                    if sum < target:
                        p3 += 1
                    elif sum > target:
                        p4 -= 1
                    elif sum == target and valueAns in valueResult:
                        p3 += 1
                        p4 -= 1
                    else:
                        valueResult.append(valueAns)
        return valueResult
# @lc code=end

