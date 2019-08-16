# queue is list of elements organized by FIFO principle
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# Hot potato game with queue
def hot_potato(names, count):
    q = Queue()

    for name in names:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(count):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()


# print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7))
