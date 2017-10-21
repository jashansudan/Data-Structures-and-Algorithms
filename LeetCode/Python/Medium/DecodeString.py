class Solution:
    def decodeString(self, s):
        numStk = []
        letters = []
        result = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                while s[i + 1].isdigit():
                    i += 1
                    num = num * 10 + int(s[i])
                numStk.append(num)
            elif s[i] == ']':
                n = numStk.pop()
                string = ""
                while letters[len[letters] - 1] != '[':
                    string = letters.pop() + string
                letters.pop()
                string = string * n
                letters.append(string)
            else:
                letters.append(s[i])
            i += 1

        while letters:
            result = letters.pop() + result
        return result
