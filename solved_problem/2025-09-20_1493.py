class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        #Set up window
        left, right = 0, 0

        #track zero occurrence
        zeros = 0

        #track longest length of subarray
        maxC = 0

        #right go first and go through each index in nums list
        #left alway behind right
        for right in range(len(nums)):
            #if there is zero then count
            if nums[right] == 0:
                zeros += 1

            #when zeros more than 1, which is wrong
            while zeros > 1:
                #if left currently at 0 then decrease one 0 from zeros
                if nums[left] == 0:
                    zeros -= 1
                #then move left one index OR keep moving left until at 0    
                left += 1

            #greedy to keep longest count // right - left = length of subarray
            maxC = max(maxC, right - left)

        return maxC