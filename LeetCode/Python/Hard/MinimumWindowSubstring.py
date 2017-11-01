class Solution:
    def minWindow(self, s, t):
        count = [0] * 256
        missing = 0
        for i in t:
            count[ord(i)] += 1
            if count[ord(i)] == 1:
                missing += 1
        string_count = [0] * 256
        min_window = "A" * (len(s) + 1)
        start = 0
        end = 0
        while end < len(s):
            string_count[ord(s[end])] += 1
            if string_count[ord(s[end])] == count[ord(s[end])]:
                missing -= 1
            while missing == 0 and start <= end:
                if end - start + 1 < len(min_window):
                    min_window = s[start:end + 1]
                string_count[ord(s[start])] -= 1
                if string_count[ord(s[start])] < count[ord(s[start])]:
                    missing += 1
                start += 1

            end += 1

        if len(min_window) == len(s) + 1:
            return ""
        return min_window
