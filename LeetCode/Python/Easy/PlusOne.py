class Solution:
    def plusOne(self, digits):
        length = len(digits) - 1
        while length >= 0:
            if digits[length] < 9:
                digits[length] += 1
                return digits
            elif digits[length] == 9:
                digits[length] = 0
                if length == 0:
                    digits.insert(0, 1)
            length -= 1
        return digits
