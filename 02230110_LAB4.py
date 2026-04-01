# Implemented by partner 2(Tenzin Lhamo)
# # Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedQueue class
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        print("Created new LinkedQueue")

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self._size += 1
        print(f"Enqueued {element} to the queue")
        self.display_list_format()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        removed = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._size -= 1
        print(f"Dequeued element: {removed}")
        return removed

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    def size(self):
        return self._size

    # Display in [10,20,30] format
    def display_list_format(self):
        temp = self.front
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(f"Display queue:[{','.join(elements)}]")

    # Display in 20 -> 30 -> null format
    def display(self):
        temp = self.front
        print("Current queue:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# Driver code
q = LinkedQueue()
print("Queue is empty:", q.is_empty())

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.peek()

q.dequeue()
q.display()

print("Queue size:", q.size())