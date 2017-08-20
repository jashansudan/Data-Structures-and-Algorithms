import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        wordCount = collections.Counter()
        for num in nums:
            wordCount[num] += 1

        frequency = [None] * (len(nums) + 1)

        for key in wordCount.keys():
            if frequency[wordCount[key]] is None:
                frequency[wordCount[key]] = [key]
            else:
                frequency[wordCount[key]].append(key)

        result = []

        for i in range(len(frequency) - 1, 0, -1):
            if len(result) == k:
                break
            if frequency[i] is not None:
                for num in frequency[i]:
                    result.append(num)

        return result
