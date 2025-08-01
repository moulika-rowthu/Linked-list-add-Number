class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Single:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="--->")
            temp = temp.next
        print("None")

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def add_position(self, pos, data):
        new_node = Node(data)
        if pos == 1: 
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        count = 1
        while temp and count < pos-1:  
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

s1 = Single()
s1.add_end(10)
s1.add_end(20)
s1.add_end(30)
s1.add_end(40)
s1.add_end(50)

print("Original List:")
s1.display()
s1.add_position(3, 25)

print("After inserting 25 at 3rd position:")
s1.display()
