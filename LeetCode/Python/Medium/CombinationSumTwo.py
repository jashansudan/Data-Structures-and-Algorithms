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

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break
            self.combinationHelper(candidates, i + 1, curr + [candidates[i]],
                                   result, target - candidates[i])
