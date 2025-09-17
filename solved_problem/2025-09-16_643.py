class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Handle edge case: if nums is empty or k is larger than nums length
        # if not nums or k > len(nums):
        #     return 0.0
        
        # Calculate the sum of the first window of size k
        curr_sum = sum(nums[:k])
        #print(curr_sum)
        max_sum = curr_sum
        
        # Slide the window and update the sum
        for i in range(len(nums) - k):
            # Remove the first element of the previous window and add the next element
            curr_sum = curr_sum - nums[i] + nums[i + k]
            print(curr_sum)
            max_sum = max(max_sum, curr_sum)
        
        # Return the maximum average
        return max_sum / k
        

        #nums = [1,12,-5,-6,50,3]  
        #       -  -   -  -      => cur = 4 => max = 4
        #          -   -  - -

        #Space Complexity: O(1) 
        #Time complexity: O(n) through for loop one time
