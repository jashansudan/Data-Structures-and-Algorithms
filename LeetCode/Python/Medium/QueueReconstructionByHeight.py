class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: x[1])
        people.sort(key=lambda x: -x[0])
        result = []
        for person in people:
            result.insert(person[1], person)

        return result
