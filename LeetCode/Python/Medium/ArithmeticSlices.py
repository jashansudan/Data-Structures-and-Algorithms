class Solution(object):
    def numberOfArithmeticSlices(self, A):
        count = 0
        if len(A) < 3:
            return count
        curr = 0
        for i in range(2, len(A)):
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]):
                curr += 1
                count += curr
            else:
                curr = 0
        return count
