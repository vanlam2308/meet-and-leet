class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        left_prod, right_prod = [1], [1] #Cumprod left and right
        for num in nums:
            left_prod.append(left_prod[-1]*num)
        for num in nums[::-1]:
            right_prod.append(right_prod[-1]*num)
        right_prod = right_prod[::-1]
        # print(left_prod, right_prod)
        # [1,2,3,4]
        # [1,1,2,6,24] Left cumprod
        # [24,24,12,4,1] Right cumprod
        # [24,12,8,6] 
        res = []
        for i in range(len(nums)):
            res.append(left_prod[i] * right_prod[i+1])
        return res