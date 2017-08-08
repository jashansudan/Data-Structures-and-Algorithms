class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if (len(self.minStack) < 1):
            self.minStack.append(x)
        else:
            if (self.minStack[-1] >= x):
                self.minStack.append(x)

    def pop(self):
        if (self.stack[-1] == self.minStack[-1]):
            self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
