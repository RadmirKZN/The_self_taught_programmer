class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def bequeue (self):
        return self.items.pop()

    def size(self):
        return len(self.items)
#1
a_queue = Queue()
print(a_queue.is_empty())
#2
a_queue = Queue()
for i in range(5):
    a_queue.enqueue(i)
print(a_queue.size())
#3
a_queue = Queue()

for i in range(5):
    a_queue.enqueue(i)
for i in range(5):
    print(a_queue.bequeue())

print()

print(a_queue.size)



