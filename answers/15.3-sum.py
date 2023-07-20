#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        result = []
        p1 = 0
        p2 = 1
        p3 = len(nums)-1
        while True:
            sum  = 0
            for i in range(p1+1, p3):
                p2 = i
                print(p2)
                sum = nums[p1] + nums[p2] + nums[p3]
                if sum > 0:

                    p3 -= 1
                    break
                elif sum  == 0:

                    if [nums[p1], nums[p2],nums[p3]] not in result:
                        result.append([nums[p1], nums[p2],nums[p3]])


            if p1+1 == p2 and p2+1 == p3:
                break
            if sum <= 0 and p2+1 == p3:

                p1 += 1
            if sum > 0  and p2+1 == p3:
                p3 -= 1

        return result
# @lc code=end

