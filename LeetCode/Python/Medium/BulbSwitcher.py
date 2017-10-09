class Solution:
    def bulbSwitch(self, n):
        num = 1
        count = 0
        while num * num <= n:
            count += 1
            num += 1
        return count
