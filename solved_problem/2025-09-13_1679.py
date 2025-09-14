# [1,2,3,4] k = 5 -> {4:0, 3:0}, count = 2
# [3,1,3,4,3] k = 6 -> {3:1, 5:1, 2:1}, count = 1 
# [2,2,2,3,1,1,4,1], k = 4 -> {2:1,1:0,}

class Solution:    
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = 0
        seen = {} # {key:value} -> {difference (k-val): occurences}
        for num in nums:
            diff = k-num
            if num in seen:
                count+=1
                seen[num]-=1
                if seen[num] == 0:
                    del seen[num]
            else:
                if diff in seen:
                    seen[diff] += 1
                else:
                    seen[diff] = 1
            # print(num, seen, count)
        return count


