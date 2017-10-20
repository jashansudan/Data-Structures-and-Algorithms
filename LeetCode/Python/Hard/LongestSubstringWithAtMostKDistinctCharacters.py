class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return k
        maxSize = 0
        start = 0
        end = 0
        characters = 0
        c = [0] * 128
        while end < len(s):
            c[ord(s[end]) - ord('a')] += 1
            if c[ord(s[end]) - ord('a')] == 1 and characters == k:
                while start < end:
                    c[ord(s[start]) - ord('a')] -= 1
                    if c[ord(s[start]) - ord('a')] == 0:
                        start += 1
                        break
                    start += 1
            elif c[ord(s[end]) - ord('a')] == 1 and characters < k:
                characters += 1
            maxSize = max(maxSize, end - start + 1)
            end += 1
        return maxSize
