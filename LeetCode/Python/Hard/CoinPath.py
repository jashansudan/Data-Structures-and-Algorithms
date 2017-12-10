class Solution:
    def cheapestJump(self, A, B):
        cost = [float('inf')] * len(A)
        cost[0] = A[0]
        jump = [-1] * len(A)
        jump[0] = A[0]
        length = [1] * len(A)
        for i in range(1, len(A)):
            if A[i] == -1:
                continue
            count = max(0, i - B)
            while count < i:
                if jump[count] != -1:
                    if cost[i] > cost[count] or cost[i] == cost[count] and length[i] < length[count] + 1:
                        cost[i] = cost[count]
                        jump[i] = count
                        length[i] = length[count] + 1
                count += 1
            cost[i] += A[i]

        if jump[len(A) - 1] == -1:
            return []

        result = [len(A)]
        curr = len(A) - 1
        while curr != 0:
            curr = jump[curr]
            result.append(curr + 1)
        return result[::-1]
