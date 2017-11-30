class Solution(object):
    def generatePossibleNextMoves(self, s):
        if len(s) < 2:
            return []

        result = []
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                if s[i] == "+":
                    result.append(s[:i - 1] + "--" + s[i + 1:])
                else:
                    result.append(s[:i - 1] + "++" + s[i + 1:])
        return result
