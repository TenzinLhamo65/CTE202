#implemented by partner 1(chador pem)
class ArrayQueue:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._data = [None] * capacity
        # Variables to track front and rear
        self._front = 0
        self._rear = -1
        self._size = 0
        self._capacity = capacity
        print(f"Created new Queue with capacity: {capacity}")
# Check if queue is empty
    def is_empty(self):
        return self._size == 0
# Example usage
q = ArrayQueue()
print("Queue is empty:", q.is_empty())
#Task 2
class ArrayQueue:
    def __init__(self, capacity=10):
        # Private array to store elements
        self._data = [None] * capacity
        
        # Front and rear pointers
        self._front = 0
        self._rear = -1
        
        # Size and capacity
        self._size = 0
        self._capacity = capacity
        
        print(f"Created new Queue with capacity: {capacity}")
# Check if queue is empty
    def is_empty(self):
        return self._size == 0
# 1. Enqueue operation
    def enqueue(self, element):
        if self._size == self._capacity:
            print("Queue is full")
            return
        self._rear = (self._rear + 1) % self._capacity
        self._data[self._rear] = element
        self._size += 1
        print(f"Enqueued {element} to the queue")
# 2. Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        element = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        print(f"Dequeued element: {element}")
        return element
# 3. Peek operation
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        print(f"Front element: {self._data[self._front]}")
        return self._data[self._front]
# 4. Size of queue
    def size(self):
        return self._size
# 5. Display queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        elements = []
        index = self._front
        for _ in range(self._size):
            elements.append(self._data[index])
            index = (index + 1) % self._capacity
            print("Display queue:", elements)
# Example usage
q = ArrayQueue()
q.enqueue(10)
q.display()
q.enqueue(20)
q.display()
q.enqueue(30)
q.display()
q.peek()
q.dequeue()
print("Current queue:", end=" ")
q.display()

