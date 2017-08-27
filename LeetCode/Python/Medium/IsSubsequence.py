class Solution(object):
    def isSubsequence(self, s, t):
        if (len(s) > len(t)):
            return False
        sPtr, tPtr = 0, 0
        while (sPtr < len(s) and tPtr < len(t)):
            if (s[sPtr] == t[tPtr]):
                sPtr += 1
            tPtr += 1
        return True if sPtr == len(s) else False
