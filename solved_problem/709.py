class Solution(object):
    def toLowerCase(self, s):
        result = ""
        for char in s:
            if 65 <= ord(char) <= 90:
                result += chr(ord(char) + 32)
            else:
                result += char

        return result 