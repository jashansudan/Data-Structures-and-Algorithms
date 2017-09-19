class Solution(object):
    def simplifyPath(self, path):
        arr = path.split('/')
        stk = []
        for i in arr:
            if i == '..':
                if stk:
                    stk.pop()
            elif i == '.' or i == '':
                continue
            else:
                stk.append(i)

        result = ''
        while stk:
            result = '/' + stk.pop() + result

        if len(result) < 1:
            return '/'
        return result
