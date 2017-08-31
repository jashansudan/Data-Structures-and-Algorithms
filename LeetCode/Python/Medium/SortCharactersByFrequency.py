class Solution(object):
    def frequencySort(self, s):
        charCounts = collections.Counter(s)

        bucket = [[] for i in range(len(s) + 1)]

        for key in charCounts.keys():
            bucket[charCounts[key]].append(key)

        frequency = ''
        for numbBucket in range(len(s), -1, -1):
            for buck in bucket[numbBucket]:
                frequency = frequency + buck * numbBucket

        return frequency

