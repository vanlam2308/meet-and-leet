class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        curr, gcd = "", ""
        for i in range(n1):
            curr += str1[i] #Substring that start from left
            if (n1 % (i+1) == 0) & (n2 % (i+1) == 0): #If len substring divide len string
                str1_temp = curr * (n1 // (i+1)) #Replicate string 1
                str2_temp = curr * (n2 // (i+1)) #Replicate string 2
                # print(curr, str1_temp, str2_temp)
                if (str1_temp == str1) & (str2_temp == str2):
                    gcd = curr
        return gcd