class Solution(object):
    def strStr(self, haystack, needle):
        if (len(needle) < 1):
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if (haystack[i] == needle[0]):
                if (haystack[i: i + len(needle)] == needle):
                    return i
        return -1
