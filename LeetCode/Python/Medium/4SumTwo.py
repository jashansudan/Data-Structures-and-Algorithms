class Solution(object):
    def fourSumCount(self, A, B, C, D):
        sums = collections.Counter()
        count = 0
        for i in A:
            for j in B:
                sums[i + j] += 1

        for k in C:
            for l in D:
                if (sums[0 - k - l] > 0):
                    count += sums[0 - k - l]

        return count
