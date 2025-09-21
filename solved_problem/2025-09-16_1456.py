class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Space/Time complexity: O(1)/O(n)
        vowels = 'ueoai'
        
        #First k
        cur = 0
        for i in range(0, k): 
            if s[i] in vowels: cur += 1

        res = cur 
        # Sliding window
        for i in range(k, len(s)):
            # Subtract number of vowel from the left of the window
            # Add number of vowel from the right boundary of the window
            cur = cur + int(s[i] in vowels) - int(s[i-k] in vowels) 
            res = max(cur, res) # greedy
        return res
