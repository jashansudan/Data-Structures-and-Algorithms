class Solution(object):
    def generateParenthesis(self, n):
        result = []
        if n < 1:
            return result

        self.parenthesisHelper(0, 0, n, '', result)
        return result

    def parenthesisHelper(self, frontBrace, backBrace, max, current, result):
        if len(current) == max * 2:
            result.append(current)
            return
        else:
            if frontBrace < max:
                self.parenthesisHelper(frontBrace + 1,
                                       backBrace, max, current + '(', result)
            if backBrace < frontBrace:
                self.parenthesisHelper(frontBrace,
                                       backBrace + 1,
                                       max, current + ')', result)
