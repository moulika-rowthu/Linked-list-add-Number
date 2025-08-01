class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Single:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="--->")
            temp = temp.next
        print("None")

    
    def get_nth_node(self, n):
        temp = self.head
        count = 1
        while temp:
            if count == n:
                return temp.data
            count += 1
            temp = temp.next
        return None  


s1 = Single()
s1.add_end(10)
s1.add_end(20)
s1.add_end(30)
s1.add_end(40)
s1.add_end(50)

print("Linked List:")
s1.display()

n = 2
result = s1.get_nth_node(n)
if result is not None:
    print(f"Data at {n}th node from head is:", result)
else:
    print(f"Position {n} is out of range")
