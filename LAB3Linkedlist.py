# Linked List-based Stack
# Implementated by partner 2(Tenzin Lhamo)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self.__size = 0
        print("Created new LinkedStack")

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self.__size += 1
        print(f"Pushed {element} to the stack")
        self.display_list_format()

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        self.__size -= 1
        print(f"Popped element: {popped_data}")
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.__size

    def display_list_format(self):
        if self.is_empty():
            print("Display stack: []")
        else:
            current = self.top
            elements = []
            while current:
                elements.append(str(current.data))
                current = current.next
            print("Display stack: [" + ",".join(elements) + "]")

    def display_arrow_format(self):
        if self.is_empty():
            print("Current stack: null")
        else:
            current = self.top
            elements = []
            while current:
                elements.append(str(current.data))
                current = current.next
            print("Current stack:", " -> ".join(elements) + " -> null")


print("\n--- LinkedStack Example ---")
linked_stack = LinkedStack()
print("Stack is empty:", linked_stack.is_empty())

linked_stack.push(10)
linked_stack.push(20)
linked_stack.push(30)

print("Top element:", linked_stack.peek())
linked_stack.pop()
linked_stack.display_arrow_format()
print("Stack size:", linked_stack.size())