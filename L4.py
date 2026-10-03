# LEETCODE 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Python solution
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
# Java solution
class Solution:
    public int[] runningSum(int[] nums) {
        int ans[] = new int[nums.length];
        ans[0] = nums[0];  

        for (int i = 1; i < nums.length; i++) {
            ans[i] = ans[i - 1] + nums[i];
        }

        return ans;

    }

    #LEETCODE 3005. Count Elements with Maximum Frequency
    # Given an integer array nums, return the number of elements that have the maximum frequency.

    class Solution:
        public int countMaxFrequency(int[] nums) {
            int maxFreq = 0;
            Map<Integer, Integer> freqMap = new HashMap<>();
            for (int num : nums) {
                freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
                maxFreq = Math.max(maxFreq, freqMap.get(num));
            }
            int count = 0;
            for (int freq : freqMap.values()) {
                if (freq == maxFreq) {
                    count++;
                }
            }
            return count;
        }
    }