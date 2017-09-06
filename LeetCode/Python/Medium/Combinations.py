class Solution(object):
    def combine(self, n, k):
        result = []
        if n < 1 or k == 0:
            return result

        self.combineHelper(n, k, result, [], 1)
        return result

    def combineHelper(self, n, k, result, curr, index):
        if index > n:
            return
        if k == 0:
            result.append(curr)
        else:
            for i in range(index, n - k + 1):
                self.combineHelper(n, k - 1, result, curr + [i], i + 1)
        return
