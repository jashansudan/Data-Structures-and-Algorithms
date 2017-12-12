class Solution:
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        lis = [1] * len(nums)
        num_seq = [0] * len(nums)
        max_len = 1
        num_lis = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lis[i] < lis[j] + 1:
                        lis[i] = lis[j] + 1
                        num_seq[i] = num_seq[j]
                    elif lis[i] == lis[j] + 1:
                        num_seq[i] += num_seq[j]
            num_seq[i] = max(1, num_seq[i])
            if lis[i] > max_len:
                max_len = lis[i]
                num_lis = num_seq[i]
            elif lis[i] == max_len:
                num_lis += num_seq[i]
        return num_lis
