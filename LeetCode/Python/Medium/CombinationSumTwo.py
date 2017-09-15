class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.combinationHelper(candidates, target, result, 0, [])
        return result

    def combinationHelper(self, candidates, target, result, index, curr):
        if target == 0:
            result.append(curr)
            return
        if target < 0:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            self.combinationHelper(candidates, target - candidates[i], result, i + 1, curr + [candidates[i]])
