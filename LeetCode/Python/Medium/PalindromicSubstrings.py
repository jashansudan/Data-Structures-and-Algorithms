class Solution:
    def countSubstrings(self, s):
        count = len(s)

        for i in range(len(s)):
            count += self.isPalindrome(s, i, i + 1)
            count += self.isPalindrome(s, i - 1, i + 1)
        return count

    def isPalindrome(self, s, first, second):
        count = 0
        while first > -1 and second < len(s):
            if s[first] == s[second]:
                count += 1
            else:
                break
            first -= 1
            second += 1
        return count
