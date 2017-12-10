class Solution:
    def repeatedStringMatch(self, A, B):
        curr = ""
        count = 0
        while len(curr) < len(B):
            count += 1
            curr += A
        if B in curr:
            return count
        if B in curr + A:
            return count + 1
        return -1
