class Solution:
    def canPermuatePalindrome(self, s):
        cCount = [0] * 128
        for i in range(len(s)):
            cCount[ord(s[i]) - ord('a')] += 1

        isOdd = False
        for i in cCount:
            if i % 2 == 1:
                if isOdd:
                    return False
                else:
                    isOdd = True
        return True
