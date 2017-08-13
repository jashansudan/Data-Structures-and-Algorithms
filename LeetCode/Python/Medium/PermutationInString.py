class Solution(object):
    def checkInclusion(self, s1, s2):
        if (len(s2) < len(s1)):
            return False

        subStringCount = [0] * 26
        stringCount = [0] * 26
        for i in range(len(s1)):
            subStringCount[ord(s1[i]) - ord('a')] += 1
            stringCount[ord(s2[i]) - ord('a')] += 1

        if subStringCount == stringCount:
            return True

        count = len(s1)
        while (count < len(s2)):
            stringCount[ord(s2[count - len(s1)]) - ord('a')] -= 1
            stringCount[ord(s2[count]) - ord('a')] += 1
            if subStringCount == stringCount:
                return True
            count += 1

        return False

