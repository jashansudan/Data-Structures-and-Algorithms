class Solution:
    def validPalindrome(self, s):
        return self.checkPalindrome(0, len(s) - 1, False)

    def checkPalindrome(self, s, low, high, skipped):
        while low < high:
            if s[low] != s[high]:
                if skipped:
                    return False
                else:
                    return self.checkPalindrome(s, low + 1, high, True) or self.checkPalindrome(s, low, high - 1, True)
            else:
                low += 1
                high -= 1
        return True
