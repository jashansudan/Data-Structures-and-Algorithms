class Solution(object):
    def permute(self, nums):
        result = []
        if len(nums) < 1:
            return result

        visited = [False] * len(nums)
        self.permutations(nums, result, [], visited)
        return result

    def permutations(self, nums, result, curr, visited):
        if len(curr) == len(nums):
            result.append(curr)
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            visited[i] = True
            self.permutations(nums, result, curr + [i], visited)
            visited[i] = False
