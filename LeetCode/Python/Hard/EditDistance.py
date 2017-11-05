class Solution:
    def minDistance(self, word1, word2):
        if word1 == "" or word2 == "":
            return max(len(word1), len(word2))

        dp = [[-1 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        dp[0][0] = 0
        self.edit(word1, word2, dp)
        return dp[len(word2)][len(word1)]


    def edit(self, word1, word2, dp):
        if word1 == "" or word2 == "":
            dp[len(word2)][len(word1)] = max(len(word1), len(word2))
        if dp[len(word2)][len(word1)] == - 1:
            if word1[len(word1) - 1] == word2[len(word2) - 1]:
                dp[len(word2)][len(word1)] = self.edit(word1[:len(word1) - 1], word2[:len(word2) - 1], dp)
            else:
                sub = self.edit(word1[:len(word1) - 1], word2[:len(word2) - 1], dp)
                delete = self.edit(word1[:len(word1) - 1], word2, dp)
                add = self.edit(word1, word2[:len(word2) - 1], dp)
                dp[len(word2)][len(word1)] = min(sub, delete, add) + 1
        return dp[len(word2)][len(word1)]
