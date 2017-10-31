class Solution:
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        ways = [0] * (len(s) + 1)
        ways[0] = 1
        for i in range(len(s)):
            if int(s[i]) > 0:
                ways[i + 1] += ways[i]
            if i > 0 and 27 > int(s[i - 1:i + 1]) > 9:
                ways[i + 1] += ways[i - 1]
        return ways[len(s)]
