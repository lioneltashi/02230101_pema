# ============================
# PART 1: ARRAY-BASED QUEUE
# ============================

# Task 1: Implement ArrayQueue Class Structure
class ArrayQueue:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity   # array
        self.front = 0
        self.rear = -1
        self.count = 0
        self.capacity = capacity
        print(f"Created new Queue with capacity: {capacity}")
        print(f"Queue is empty: {self.is_empty()}")

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count


    # Task 2: Queue Operations (Array)

    def enqueue(self, element):
        if self.count == self.capacity:
            print("Queue is full!")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.count += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        element = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        print(f"Dequeued element: {element}")
        self.display()
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element: {self.queue[self.front]}")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        result = []
        for i in range(self.count):
            index = (self.front + i) % self.capacity
            result.append(self.queue[index])
        print("Display queue:", result)


# ============================
# PART 2: LINKED LIST QUEUE
# ============================

# Task 3: Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Task 3: LinkedQueue Class Structure
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
        print("Created new LinkedQueue")
        print(f"Queue is empty: {self.is_empty()}")

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count


    # Task 4: Queue Operations (Linked List)

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node

        if self.front is None:
            self.front = new_node

        self.count += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None

        element = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1
        print(f"Dequeued element: {element}")
        self.display()
        return element

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        temp = self.front
        result = ""
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        result += "null"
        print("Current queue:", result)


# ============================
# MAIN (TESTING BOTH QUEUES)
# ============================

print("\n--- ARRAY QUEUE ---")
aq = ArrayQueue()
aq.enqueue(11)
aq.enqueue(23)
aq.enqueue(5)
aq.peek()
aq.dequeue()
print("Queue size:", aq.size())

print("\n--- LINKED QUEUE ---")
lq = LinkedQueue()
lq.enqueue(11)
lq.enqueue(23)
lq.enqueue(5)
lq.peek()
lq.dequeue()
print("Queue size:", lq.size())