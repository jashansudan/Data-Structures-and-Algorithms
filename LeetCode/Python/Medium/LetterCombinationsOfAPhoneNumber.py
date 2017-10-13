class Solution:
    def letterCombinations(self, digits):
        if len(digits) < 1:
            return []
        letterArr = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs",
                     "tuv", "wxyz"]
        result = [""]
        for digit in digits:
            if digit == "1":
                continue
            newResult = []
            for temp in result:
                for char in letterArr[int(digit)]:
                    newResult.append(temp + char)
            result = newResult
        return result
