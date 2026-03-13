class CustomList:
    
    # Constructor (Task 1)
    def __init__(self):
        self.capacity = 10                # default capacity
        self.arr = [None] * self.capacity # underlying array
        self.size = 0                     # current size
        
        print("Created new CustomList with capacity:", self.capacity)
        print("Current size:", self.size)

    # 1. append(element)
    def append(self, element):
        if self.size < self.capacity:
            self.arr[self.size] = element
            self.size += 1
            print("Appended", element, "to the list")
        else:
            print("List is full")

    # 2. get(index)
    def get(self, index):
        if 0 <= index < self.size:
            return self.arr[index]
        else:
            print("Invalid index")
            return None

    # 3. set(index, element)
    def set(self, index, element):
        if 0 <= index < self.size:
            self.arr[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            print("Invalid index")

    # 4. size()
    def get_size(self):
        return self.size


# Example run
my_list = CustomList()

my_list.append(7)

print("Element at index 0:", my_list.get(0))

my_list.set(0, 10)

print("Element at index 0:", my_list.get(0))

print("Current size:", my_list.get_size())