"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   ***"Stack" of papers is = Last-in / Fist-out (LIFO)
   ***"Queue"-d in a line at the store is = First-in / First-out (FIFO)
"""


class Stack:
    def __init__(self, storage=None):
        self.storage = storage if storage is not None else []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.insert(0, value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

messing_around = Stack(a_list)


print(messing_around.__len__())
print(messing_around.storage)

print(messing_around.push(101))
print(messing_around.storage)

print(messing_around.pop())
print(messing_around.storage)

# Linked List Starts Here


# class Stack:
#     def __init__(self, storage=None):
#         self.storage = storage if storage is not None else []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.insert(0, value)

#     def pop(self):
#         return self.storage.pop(0)
