class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        first_num, second_num = float("inf"), float("inf")
        for n in nums:
            if n < first_num:
                first_num = n
            elif first_num < n < second_num:
                second_num = n
            elif n > first_num and n > second_num:
                return True
        return False
        
        # [2,1,5,0,4,6]
        # [0,4,2,1,0,-1,-3]
        # first: 0, 
        # second: 4,2,1
                
