class Solution(object):
    def lengthLongestPath(self, input):
        files = input.split('\n')
        longestPath = 0
        if len(files) < 1:
            return longestPath

        prevTabs = 0
        lengthSoFar = len(files[0])
        if '.' in files[0]:
            longestPath = lengthSoFar
        stk = []
        stk.append(files[0])

        for i in range(1, len(files)):
            numberOfTabs = (len(files[i]) - len(files[i].replace('\t', '')))
            if numberOfTabs > prevTabs:
                stk.append(files[i])
                lengthSoFar += 1 + len(files[i].replace('\t', ''))

            elif numberOfTabs == prevTabs:
                stk.pop()
                stk.append(files[i])
                lengthSoFar -= len(files[i - 1].replace('\t', ''))
                lengthSoFar += len(files[i].replace('\t', ''))
            else:
                for _ in range(prevTabs - numberOfTabs + 1):
                    temp = stk.pop()
                    lengthSoFar -= len(temp.replace('\t', '')) + 1

                stk.append(files[i])
                lengthSoFar += 1 + len(files[i].replace('\t', ''))

            prevTabs = numberOfTabs
            if '.' in stk[len(stk) - 1]:
                longestPath = max(longestPath, lengthSoFar)

        return longestPath
