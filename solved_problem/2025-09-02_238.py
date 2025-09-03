class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        left_prod = [1] #Cumprod left and right
        for i in range(n-1):
            left_prod.append(left_prod[-1]*nums[i])

        right_prod = [1]
        for i in range(n-1):
            right_prod.append(right_prod[-1]*nums[-1-i])

        right_prod = right_prod[::-1]
        print(left_prod, right_prod)
        #   1, 2, 3, 4
        #   ^  
        # 1,1, 2, 6     #Left product
        #     24,12,4,1 #Right product
        #   24,12,8,6
        res = []
        for i in range(len(nums)):
            res.append(left_prod[i] * right_prod[i])
        return res