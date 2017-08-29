class Solution(object):
    def addDigits(self, num):
        while (num > 9):
            count = 0
            while num > 0:
                count += num % 10
                num = num / 10
            num = count
        return num
