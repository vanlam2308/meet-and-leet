class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        h_map = {5:0, 10:0, 20:0} #Tien thoi. Hash table
        for b in bills:
            if b == 5:
                h_map[5] += 1
            elif b == 10:
                h_map[10] += 1
                h_map[5] -= 1
            elif b == 20:
                h_map[20] += 1 
                if h_map[10] > 0: #Greedy algorithm
                    h_map[10] -= 1
                    h_map[5] -= 1
                else:
                    h_map[5] -= 3                    
            else:
                print("Invalid")
                return False  
            if (h_map[5] < 0) or (h_map[10] < 0):
                return False
        return True
        
# Space Complexity: O(1) => 5, 10, 20
# Time Complexity: O(n) => number of bills
