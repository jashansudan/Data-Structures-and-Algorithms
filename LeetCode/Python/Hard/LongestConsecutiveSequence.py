class Solution:
    def longestConsecutive(self, nums):
        seq_map = {}
        max_seq = 0
        for i in range(len(nums)):
            if nums[i] in seq_map:
                continue

            higher = 0
            if (nums[i] + 1) in seq_map:
                higher = seq_map[nums[i] + 1]
            lower = 0
            if nums[i] - 1 in seq_map:
                lower = seq_map[nums[i] - 1]

            total = lower + higher + 1
            seq_map[nums[i]] = total
            seq_map[nums[i] + higher] = total
            seq_map[nums[i] - lower] = total
            max_seq = max(max_seq, total)
        return max_seq
