class CustomList:

    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__size = 0
        self.__array = [None] * capacity

        print("New CustomList with capacity:", self.__capacity)
        print("Current size:", self.__size)

    def append(self, element):
        if self.__size == self.__capacity:
            print("List is full")
            return

        self.__array[self.__size] = element
        self.__size += 1
        print(f"Appended {element} to the list")

    def get(self, index):
        if index < 0 or index >= self.__size:
            print("Index out of bounds")
            return None

        return self.__array[index]

    def set(self, index, element):
        if index < 0 or index >= self.__size:
            print("Index out of bounds")
            return

        self.__array[index] = element
        print(f"Set element at index {index} to {element}")

    def size(self):
        return self.__size


# Testing the list
my_list = CustomList()

my_list.append(5)

print("Element at index 0:", my_list.get(0))

my_list.set(0, 10)

print("Element at index 0:", my_list.get(0))

print("Current size:", my_list.size())