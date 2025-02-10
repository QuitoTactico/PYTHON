class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop() if self.queue else None

    def peek(self):
        return self.queue[-1] if self.queue else None

    def is_empty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)
