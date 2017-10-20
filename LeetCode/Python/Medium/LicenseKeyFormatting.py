class Solution:
    def licenseKeyFormatting(self, S, K):
        end = len(S) - 1
        newFormat = ""
        count = 0
        while end > -1:
            if S[end] != '-':
                if count == K:
                    newFormat = "-" + newFormat
                    count = 0
                    continue
                else:
                    newFormat = S[end].upper() + newFormat
                    count += 1
            end -= 1
        return newFormat
