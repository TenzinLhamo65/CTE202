'''#part 1
#Task 1
class ArrayStack:
    def __init__(self, capacity=10):
        self.stack = [None] * capacity   # Array to store elements
        self.top = -1                    # Top of stack
        self.capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")
    # Check if stack is empty
    def is_empty(self):
        return self.top == -1
# Main program to test
if __name__ == "__main__":
    stack = ArrayStack()
    print("Stack is empty:", stack.is_empty())'''
#task 2
class ArrayStack:
    def __init__(self, capacity=10):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity
# 1. Push operation
    def push(self, element):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = element
            print(f"Pushed {element} to the stack")
# 2. Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        else:
            element = self.stack[self.top]
            self.top -= 1
            print(f"Popped element: {element}")
            return element

    # 3. Peek operation
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.stack[self.top]
# 4. Check if empty
    def is_empty(self):
        return self.top == -1
# 5. Size of stack
    def size(self):
        return self.top + 1
# 6. Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Display stack:", self.stack[:self.top + 1])
# Main program
if __name__ == "__main__":
    stack = ArrayStack()
    stack.push(10)
    stack.display()
    stack.push(20)
    stack.display()
    stack.push(30)
    stack.display()
    print("Top element:", stack.peek())
    stack.pop()
    print("Stack size:", stack.size())
    stack.display()