class Solution(object):
    def countBinarySubstrings(self, s):

        group = [1]

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                group[-1] += 1
            else:
                group.append(1)

        res = 0
        for i in range(len(group) - 1):
            res += min(group[i], group[i + 1])
        
        return res 