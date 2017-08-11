class Solution(object):
    def combinationSum3(self, k, n):
        if n > 45 or n == 1:
            return []
        result = []
        self.combinationHelper(k, n, 1, result, [])
        return result

    def combinationHelper(self, k, n, index, result, curr):
        if len(curr) == k and n == 0:
            result.append(curr)
            return
        if len(curr) > k or index > 9:
            return
        else:
            for i in range(index, 10):
                self.combinationHelper(k, n - i, i + 1, result, curr + [i])
