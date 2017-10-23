class MovingAverage(object):
    def __init__(self, size):
        self.arr = [0] * size
        self.elements = 0
        self.total = 0

    def next(self, val):
        if self.elements < len(self.arr):
            self.arr[self.elements] = val
            self.total += val
            self.elements += 1
            return self.total / float(self.elements)
        else:
            self.total -= self.arr[self.elements % len(self.arr)]
            self.arr[self.elements % len(self.arr)] = val
            self.total += val
            self.elements += 1
        return self.total / float(len(self.arr))
