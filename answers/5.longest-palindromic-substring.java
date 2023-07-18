/*
 * @lc app=leetcode id=5 lang=java
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        String res = new String();
        int[][] t = new int[s.length()][s.length()];
        return res;
    }
    public boolean dp(String s, Integer i, Integer j, int[][] temp){
        if (i == j){
            return dp(s, i, j+1);
        }
        if(s.charAt(i) == s.charAt(j))
        return false;
    }
}
// @lc code=end

