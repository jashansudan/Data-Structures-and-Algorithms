class Solution(object):
    def isValid(self, s):
        stk = []

        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stk.append(bracket)
            else:
                if not stk:
                    return False
                else:
                    if bracket == ')' and stk[len(stk) - 1] == '(':
                        stk.pop()
                    elif bracket == ']' and stk[len(stk) - 1] == '[':
                        stk.pop()
                    elif bracket == '}' and stk[len(stk) - 1] == '{':
                        stk.pop()
                    else:
                        return False

        return False if stk else True
