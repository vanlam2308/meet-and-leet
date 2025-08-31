class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0] #Add 2 empty plots to maintain the flow
        for i in range(1,len(flowerbed)-1): #Skip those 2 extra plots
            if (flowerbed[i] == flowerbed[i-1] == flowerbed[i+1]==0): #If 3 plots are empty
                flowerbed[i] -= 1
                n -= 1
        return n <= 0