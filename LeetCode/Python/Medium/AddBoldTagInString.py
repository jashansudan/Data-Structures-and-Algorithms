class Solution:
    def addBoltTag(self, s, dict):
        bold_tags = [False] * len(s)

        for word in dict:
            for i in range(len(s)):
                if s[i:i + len(word)] == word:
                    for mark_true in range(i, i + len(word)):
                        bold_tags[mark_true] = True

        new_str = ""
        prev_tag = False
        for i in range(len(s)):
            if bold_tags[i]:
                if not prev_tag:
                    new_str += "<b>"
                    prev_tag = True
            else:
                if prev_tag:
                    new_str += "</b>"
                    prev_tag = False

            new_str += s[i]
        if prev_tag:
                new_str += "</b>"
        return new_str
