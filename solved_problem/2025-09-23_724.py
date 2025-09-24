class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums) #Time: O(n), Space: O(1)
        current_sum = 0 #Left sum
        for i in range(len(nums)):
            if current_sum == total - current_sum - nums[i]:
                return i
            current_sum += nums[i]
        return -1
#Time: O(n), Space: O(1)
# How to implement built in sum
# sum_ = 0
# for i in range(len(nums)):
#     sum_+=nums[i]
