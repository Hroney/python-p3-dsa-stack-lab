class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        if self.size() == self.limit:
            pass
        else:
            self.items.append(item)
        pass

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        depth = self.size() - 1
        for value in self.items:
            if value == target:
                return depth
            else:
                depth -= 1
        return -1
