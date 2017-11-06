class Solution:
    def wallsAndGates(self, rooms):
        if rooms is None:
            return rooms

        gates = []
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    gates.append([row, col])

        for i in gates:
            q = collections.deque()
            q.append(i)
            counter = -1
            size = 0
            while q:
                if size == 0:
                    size = len(q)
                    counter += 1
                temp = q.popleft()
                if rooms[temp[0]][temp[1]] == -1:
                    size -= 1
                    continue
                if rooms[temp[0]][temp[1]] < counter:
                    size -= 1
                    continue
                if rooms[temp[0]][temp[1]] != 0:
                    rooms[temp[0]][temp[1]] = counter
                if temp[0] > 0:
                    q.append([temp[0] - 1, temp[1]])
                if temp[0] < len(rooms) - 1:
                    q.append([temp[0] + 1, temp[1]])
                if temp[1] > 0:
                    q.append([temp[0], temp[1] - 1])
                if temp[1] < len(rooms[0]) - 1:
                    q.append([temp[0], temp[1] + 1])

                size -= 1
        return
