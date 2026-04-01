# =======================
# Part 1: Array-based Stack
# =======================

# Task 1
class ArrayStack:
    def __init__(self, capacity=15):
        self._stack = [None] * capacity  # Private array
        self._top = -1  # Index of top element
        self._capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")
        print(f"Stack is empty: {self.is_empty()}")
#Task 2
    # Push element to top of stack
    def push(self, element):
        if self._top >= self._capacity - 1:
            # Resize array if full
            self._capacity *= 2
            new_stack = [None] * self._capacity
            for i in range(self._top + 1):
                new_stack[i] = self._stack[i]
            self._stack = new_stack
        self._top += 1
        self._stack[self._top] = element
        print(f"Pushed {element} to the stack")
        self.display()

    # Pop element from top
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        element = self._stack[self._top]
        self._stack[self._top] = None  # Optional: clear reference
        self._top -= 1
        print(f"Popped element: {element}")
        self.display()
        return element

    # Peek top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        print(f"Top element: {self._stack[self._top]}")
        return self._stack[self._top]

    # Check if stack is empty
    def is_empty(self):
        return self._top == -1

    # Return size of stack
    def size(self):
        return self._top + 1

    # Display stack elements
    def display(self):
        if self.is_empty():
            print("Display stack: []")
        else:
            print("Display stack:", self._stack[:self._top + 1])

if __name__ == "__main__":
    print("=== ArrayStack Example ===")
    array_stack = ArrayStack()
    array_stack.push(15)
    array_stack.push(31)
    array_stack.push(23)
    array_stack.peek()
    array_stack.pop()
    print(f"Stack size: {array_stack.size()}\n")
