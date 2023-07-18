/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        HashMap <Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i =0; i<nums.length; i++){
            map.put(nums[i], i);
        }
        for(int i = 0; i<nums.length; i++){
            if(map.keySet().contains(target-nums[i]) && i!=map.get(target-nums[i])){
                result[0] = i;
                result[1] = map.get(target-nums[i]);
            }
        }
        return result;
    }
}
// @lc code=end

