# Node is element of unordered list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def set_data(self, data):
        self.data = data


# Unordered list - each element has link only to the next element
class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        new_item = Node(item)
        new_item.set_next(self.head)
        self.head = new_item

    def size(self):
        count = 0
        head = self.head
        while head != None:
            head = head.get_next()
            count += 1

        return count

    def search(self, value):
        current = self.head
        found = False
        while current != None and (not found):
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        prev = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                prev = current
                current = current.get_next()
        if prev == None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())



ul = UnorderedList()
ul.add('1')
ul.add('2')
ul.add('3')
ul.add('4')
ul.add('5')
print(ul.size())
print(ul.search('5'))
ul.remove('3')
print(ul.size())
