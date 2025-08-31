class Solution(object):
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        boolList = []
        largest = max(candies)

        for candy in candies:
            if candy + extraCandies >= largest:
                boolList.append(True)
            else:
                boolList.append(False)
        
        return boolList