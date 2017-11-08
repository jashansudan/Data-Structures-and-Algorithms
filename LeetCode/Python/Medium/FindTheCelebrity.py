class Solution:
    def findCelebrity(self, n):
        if n == 0:
            return - 1
        celeb = 0

        for i in range(1, n):
            if knows(celeb, i):
                celeb = i

        for i in range(n):
            if knows(celeb, i) and celeb != i:
                return -1
            if not knows(i, celeb):
                return -1
        return celeb
