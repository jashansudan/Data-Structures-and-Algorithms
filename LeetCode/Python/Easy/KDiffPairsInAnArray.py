class Solution(object):
    def findPairs(self, nums, k):
        pairs = 0
        collect = Counter(nums)
        for i in collect:
            if k > 0 and i + k in collect or k == 0 and collect[i] > 1:
                pairs += 1
        return pairs
