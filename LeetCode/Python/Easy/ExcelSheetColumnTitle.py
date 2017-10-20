class Solution(object):
    def convertToTitle(self, n):
        title = ""
        while n > 0:
            n -= 1
            title = chr(ord('A') + (n % 26)) + title
            n /= 26
        return title
