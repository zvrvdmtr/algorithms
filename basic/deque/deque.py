# deque is a list of elements organized by LIFO and FIFO principle simultaneously
class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()


# Palindrome checker realization using deque
def palindrome_checker(word):
    palindrome = True
    d = Deque()

    for i in word:
        d.add_rear(i)

    while palindrome and d.size() > 1:
        front = d.remove_front()
        rear = d.remove_rear()
        if front != rear:
            palindrome = False

    return palindrome



print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))