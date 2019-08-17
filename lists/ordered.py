from lists.node import Node


# Ordered list - each element has link only to the next element and arranged in order (ASC, DESC)
class OrderedList:

    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = None

        while not found and current and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while not stop and current != None:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        new_item = Node(item)

        if previous == None:
            new_item.set_next(self.head)
            self.head = new_item
        else:
            new_item.set_next(current)
            previous.set_next(new_item)

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            current = current.get_next()
            count += 1

        return count


ol = OrderedList()
ol.add('1')
ol.add('2')
ol.add('4')
ol.add('5')
ol.add('3')
print(ol.size())