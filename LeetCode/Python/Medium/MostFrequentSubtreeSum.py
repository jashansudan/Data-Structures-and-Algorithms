class Solution(object):
    def findFrequentTreeSum(self, root):
        dictionary = {}

        self.subTreeSum(root, dictionary)

        maxCount = 0
        maxes = []
        for keys in dictionary.keys():
            if dictionary[keys] > maxCount:
                maxCount = dictionary[keys]
                maxes = [keys]
            elif dictionary[keys] == maxCount:
                maxes.append(keys)

        return maxes

    def subTreeSum(self, root, dictionary):
        if root is None:
            return 0

        left = self.subTreeSum(root.left, dictionary)
        right = self.subTreeSum(root.right, dictionary)

        subSum = root.val + left + right

        if subSum in dictionary:
            dictionary[subSum] = dictionary[subSum] + 1
        else:
            dictionary[subSum] = 1

        return subSum
