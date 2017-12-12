class Solution:
    def hIndex(self, citations):
        low = 0
        high = len(citations) - 1
        size = high + 1
        while low <= high:
            mid = (low + high) / 2
            if citations[mid] == (size - mid):
                return citations[mid]
            elif (citations[mid] > (size - mid)):
                high = mid - 1
            else:
                low = mid + 1
        return size - (high + 1)
