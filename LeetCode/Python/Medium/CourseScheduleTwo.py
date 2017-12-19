class Solution:
    def findOrder(self, numCourses, prerequisites):
        result = []
        req = [0] * numCourses
        req_map = collections.defaultdict(list)
        queue = collections.deque()

        for i in range(len(prerequisites)):
            req[prerequisites[i][0]] += 1
            req_map[prerequisites[i][1]].append(prerequisites[i][0])

        for i in range(len(req)):
            if req[i] == 0:
                queue.append(i)
                result.append(i)

        while queue:
            course = queue.popleft()
            for i in req_map[course]:
                req[i] -= 1
                if req[i] == 0:
                    result.append(i)
                    queue.append(i)

        if len(result) == numCourses + 1:
            return result
        return []
