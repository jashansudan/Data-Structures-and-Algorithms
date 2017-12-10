class Solution:
    def addOperators(self, num, target):
        if not num:
            return []
        result = []
        for i in range(len(num)):
            if num[0] == "0" and i > 0:
                break
            else:
                self.operatorHelper(num[i + 1:], target, result, int(num[:i + 1]), 0, num[:i + 1])
        return result

    def operatorHelper(self, num, target, result, mult, total, curr):
        if num == "" and total + mult == target:
                result.append(curr)
        else:
            for i in range(len(num)):
                if num[0] == "0" and i > 0:
                    break
                else:
                    self.operatorHelper(num[i + 1:], target, result, int(num[:i + 1]), total + mult, curr + "+" + num[:i + 1])
                    self.operatorHelper(num[i + 1:], target, result, -int(num[:i + 1]), total + mult , curr + "-" + num[:i + 1])
                    self.operatorHelper(num[i + 1:], target, result, mult * int(num[:i + 1]), total,  curr + "*" + num[:i + 1])
        return
