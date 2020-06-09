"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   ***"Stack" of papers is = Last-in / Fist-out (LIFO)
   ***"Queue"-d in a line at the store is = First-in / First-out (FIFO)
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


class Queue:
    def __init__(self, storage=None):
        self.storage = storage if storage is not None else []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None


the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

some_tests = Queue(the_list)

print(some_tests.__len__())
print(some_tests.storage)

print(some_tests.enqueue(102))
print(some_tests.storage)

print(some_tests.dequeue())
print(some_tests.storage)


# Linked List Starts Here

# class Queue:
#     def __init__(self, storage=None):
#         self.storage = storage if storage is not None else []

#     def __len__(self):
#         pass

#     def enqueue(self, value):
#         pass

#     def dequeue(self):
#         pass
