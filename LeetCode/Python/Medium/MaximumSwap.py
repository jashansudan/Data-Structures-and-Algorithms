class Solution:
    def maximumSqap(self, num):
        num = str(num)
        buckets = [-1] * 10
        for i in range(len(num)):
            buckets[int(num[i])] = i

        for i in range(len(num)):
            for buc in range(9, -1, -1):
                if buc <= int(num[i]):
                    break
                if buckets[buc] > i:
                    num = num[:i] + str(buc) + num[i + 1:buckets[buc]] + num[i] + num[buckets[buc] + 1:]
                    return int(num)

        return int(num)