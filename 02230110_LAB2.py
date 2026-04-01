class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None      


# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None     
        self.tail = None     
        self._size = 0        
        print("Created new LinkedList")
        print("Current size:", self._size)
        print("Head:", self.head)

    # Append element at end
    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"Appended {element} to the list")

    # Get element at index
    def get(self, index):
        if index < 0 or index >= self._size:
            print("Index out of range")
            return None

        current = self.head
        for _ in range(index):
            current = current.next

        print(f"Element at index {index}: {current.data}")
        return current.data

    # Set element at index
    def set(self, index, element):
        if index < 0 or index >= self._size:
            print("Index out of range")
            return

        current = self.head
        for _ in range(index):
            current = current.next

        current.data = element
        print(f"Set element at index {index} to {element}")

   
    def size(self):
        print("Current size:", self._size)
        return self._size


    def prepend(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1
        print(f"Prepend {element} to the list")

  
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Print Linked list: [" + " ".join(elements) + "]")


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(5)
    ll.get(0)
    ll.set(0, 10)
    ll.get(0)
    ll.size()

    ll.prepend(10)
    ll.append(5)   
    ll.print_list()