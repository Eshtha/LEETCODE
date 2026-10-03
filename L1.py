# leetcode 1480 
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums)
        ans[0] = nums[0]
        # runningSum[n] = runningSum[n-1] + nums[n]
        for i in range(1, len(nums)):
            ans[i] = ans[i-1]+nums[i]
        return ans
    