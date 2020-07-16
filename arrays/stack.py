class Stack(object):
    def __init__(self, numbers):
        self.data = numbers

    def __len__(self):
        return len(self.data)

    def _push(self, value):
        self.data.append(value)

    def _pop(self):
        if self.data:
            self.data.pop()
        else:
            return -1

    def _empty(self):
        return 0 if self.data else -1

    def _top(self):
        return self.data[-1] if self.data else -1
