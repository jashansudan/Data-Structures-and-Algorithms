class BSTIterator(object):
    def __init__(self, root):
        self.stk = []
        self.curr = root
        while self.curr or self.stk:
            while self.curr:
                self.stk.append(self.curr)
                self.curr = self.curr.left
            break
        if self.stk:
            self.curr = self.stk.pop()

    def hasNext(self):
        if self.curr:
            return True
        return False

    def next(self):
        temp = self.curr
        self.curr = self.curr.right
        while self.curr or self.stk:
            while self.curr:
                self.stk.append(self.curr)
                self.curr = self.curr.left
            break
        if self.stk:
            self.curr = self.stk.pop()
        return temp.val
