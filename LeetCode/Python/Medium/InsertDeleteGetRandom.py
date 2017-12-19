class RandomizedSet(object):

    def __init__(self):
        self.last_elem = 0
        self.int_map = {}
        self.int_arr = []

    def insert(self, val):
        if val in self.int_map:
            return False
        self.int_arr.append(val)
        self.int_map[val] = self.last_elem
        self.last_elem += 1
        return True

    def remove(self, val):
        if val not in self.int_map:
            return False
        self.last_elem -= 1
        self.int_map[self.int_arr[self.last_elem]] = self.int_map[val]
        self.int_arr[self.int_map[val]], self.int_arr[self.last_elem] = self.int_arr[self.last_elem],  self.int_arr[self.int_map[val]]
        self.int_arr.pop()
        del self.int_map[val]
        return True

    def getRandom(self):
        return self.int_arr[random.randint(0, self.last_elem - 1)]
