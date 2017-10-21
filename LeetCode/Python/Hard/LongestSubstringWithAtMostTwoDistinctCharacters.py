class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        nums = 2
        maxLength = 0
        start = 0
        end = 0
        c_count = [0] * 128
        while end < len(s):
            c_count[ord(s[end]) - ord('a')] += 1
            if c_count[ord(s[end]) - ord('a')] == 1 and nums == 0:
                while start < end:
                    c_count[ord(s[start]) - ord('a')] -= 1
                    if c_count[ord(s[start]) - ord('a')] == 0:
                        start += 1
                        break
                    start += 1
            elif c_count[ord(s[end]) - ord('a')] == 1 and nums > 0:
                nums -= 1
            maxLength = max(maxLength, end - start + 1)
            end += 1
        return maxLength
