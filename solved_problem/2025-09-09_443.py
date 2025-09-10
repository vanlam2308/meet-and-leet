class Solution:
    def compress(self, chars: list[str]) -> int:
        chars += "*"
        count = 1
        pointer = 0
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                count += 1
            else: #Stopping criteria
                # 1) Character
                chars[pointer] = chars[i]
                pointer += 1
                # 2) Number of occurences
                if count!=1:
                    for digit in str(count):
                        chars[pointer] = digit
                        pointer += 1
                count = 1 #Reset
        return pointer
