class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        if candidates is None:
            return result
        self.combinationHelper(candidates, target, [], result, 0)
        return result

    def combinationHelper(self, candidates, target, curr, result, index):
        if target < 0:
            return
        if target == 0:
            result.append(curr)
        else:
            for i in range(index, len(candidates)):
                self.combinationHelper(candidates,
                                       target - candidates[i],
                                       curr + [candidates[i]],
                                       result, i)
        return
