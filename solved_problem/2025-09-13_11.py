class Solution:
    def maxArea(self, height: list[int]) -> int:

        n = len(height)
        left, right = 0, n - 1 #set up left and right - two pointer solution
        max_area = 0

        while left < right: # loop from 0 to n
            area = min(height[left], height[right]) * (right - left) #multiply smaller column with space between column
            max_area = max(max_area, area) # is current area bigger than recorded area - Greedy 

            # look for higher column
            if height[left] < height[right]: 
                # move to left if left small
                left += 1
            else:
                #move to right if right small
                right -= 1

        return max_area