class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Calculate the sum of the first window of size k
        for i in range(k):
            curr_sum += nums[i]

        max_sum = curr_sum
        
        # Slide the window and update the sum
        for i in range(len(nums) - k):
            # Remove the first element of the previous window and add the next element
            curr_sum = curr_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, curr_sum)
        
        # Return the maximum average
        return max_sum / k

        #Space Complexity: O(1)
        #Time complexity: O(n) through for loop one time
