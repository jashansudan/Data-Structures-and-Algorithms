class Solution:
    result = 0

    def countArrangement(self, N):
        if N < 1:
            return self.result
        used = [False] * (N + 1)
        self.countHelper(N, used, 1)
        return self.result

    def countHelper(self, N, used, pos):
        if pos > N:
            self.result += 1
        else:
            for i in range(1, N + 1):
                if not used[i]:
                    if i % pos == 0 or pos % i == 0:
                        used[i] = True
                        self.countHelper(N, used, pos + 1)
                        used[i] = False
        return
