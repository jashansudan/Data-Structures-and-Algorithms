class Solution:
    def leastInterval(self, tasks, n):
        if not tasks:
            return 0
        task_count = [0] * 26
        for i in range(len(tasks)):
            task_count[ord(tasks[i]) - ord('A')] += 1

        task_count.sort()
        num_of_maxes = 1
        max_count = task_count[25]
        for i in range(24, -1, -1):
            if task_count[i] == max_count:
                num_of_maxes += 1

        interval = num_of_maxes * max_count
        if (n - (num_of_maxes - 1)) > 0:
            interval += (n - (num_of_maxes - 1)) * (max_count - 1)
        return max(interval, len(tasks))
